"""Tests for the GAIA-SL1 OPT-IN scaffold generator."""

import sys
from pathlib import Path

import pytest

# Ensure the generator module is importable
sys.path.append(
    str(Path(__file__).resolve().parents[1] / "01-PROGRAMS" / "GAIA-SPACE-LAUNCHER")
)

from generate_scaffold import (
    CSDB_SUBDIRS,
    LC01_TEMPLATES,
    LIFECYCLE_CODES,
    TAXONOMY,
    build_scaffold,
    taxonomy_summary,
)


# ------------------------------------------------------------------
# Taxonomy integrity tests
# ------------------------------------------------------------------


def test_taxonomy_chapter_count() -> None:
    """The taxonomy must define exactly 52 chapters."""
    s = taxonomy_summary()
    assert s["chapters"] == 52


def test_taxonomy_section_count() -> None:
    """The taxonomy must define exactly 333 sections."""
    s = taxonomy_summary()
    assert s["sections"] == 333


def test_taxonomy_axes() -> None:
    """There must be exactly 5 OPT-IN axes."""
    assert len(TAXONOMY) == 5
    expected_prefixes = {"O", "P", "T", "I", "N"}
    actual_prefixes = {k.split("-")[0] for k in TAXONOMY}
    assert actual_prefixes == expected_prefixes


def test_technology_subaxes() -> None:
    """T-TECHNOLOGIES must have 7 sub-axes."""
    t_axis = TAXONOMY["T-TECHNOLOGIES"]
    assert len(t_axis) == 7
    expected_codes = {"S", "P", "F", "E", "A", "C", "TH"}
    actual_codes = {k.split("-")[0] for k in t_axis}
    assert actual_codes == expected_codes


def test_lifecycle_codes() -> None:
    """LC01 through LC14 must be defined."""
    assert len(LIFECYCLE_CODES) == 14
    assert LIFECYCLE_CODES[0] == "LC01"
    assert LIFECYCLE_CODES[-1] == "LC14"


def test_lc01_templates_defined() -> None:
    """LC01 must carry 6 template files."""
    assert len(LC01_TEMPLATES) == 6
    names = {t[0] for t in LC01_TEMPLATES}
    assert "KNOTS.csv" in names
    assert "TOKENOMICS_TT.yaml" in names


def test_csdb_subdirs() -> None:
    """CSDB must have 7 sub-directories per S1000D conventions."""
    assert len(CSDB_SUBDIRS) == 7
    assert "DM" in CSDB_SUBDIRS
    assert "BREX" in CSDB_SUBDIRS


# ------------------------------------------------------------------
# Scaffold generation tests (use tmp_path for isolation)
# ------------------------------------------------------------------


def test_build_scaffold_stats(tmp_path: Path) -> None:
    """build_scaffold must report correct chapter/section counts."""
    stats = build_scaffold(tmp_path / "scaffold")
    assert stats["chapters"] == 52
    assert stats["sections"] == 333
    assert stats["files"] > 0
    assert stats["dirs"] > 0


def test_root_readme_created(tmp_path: Path) -> None:
    """The scaffold root must have a README."""
    root = tmp_path / "scaffold"
    build_scaffold(root)
    assert (root / "README.md").is_file()


def test_axis_directories_created(tmp_path: Path) -> None:
    """Each OPT-IN axis must have its own directory with a README."""
    root = tmp_path / "scaffold"
    build_scaffold(root)
    for axis in TAXONOMY:
        axis_dir = root / axis
        assert axis_dir.is_dir(), f"Missing axis directory: {axis}"
        assert (axis_dir / "README.md").is_file()


def test_section_canonical_structure(tmp_path: Path) -> None:
    """Spot-check one section for the full canonical layout."""
    root = tmp_path / "scaffold"
    build_scaffold(root)

    # Pick first section of CH01
    sec = (
        root
        / "O-OPERATIONS"
        / "CH01-Launch_Operations"
        / "01-Pre-Launch_Processing"
    )
    assert sec.is_dir(), "Section directory missing"
    assert (sec / "README.md").is_file()

    # SSOT
    ssot = sec / "SSOT"
    assert (ssot / "README.md").is_file()
    assert (ssot / "LC01").is_dir()
    assert (ssot / "LC14").is_dir()

    # LC01 templates
    for fname, _ in LC01_TEMPLATES:
        assert (ssot / "LC01" / fname).is_file(), f"Missing template: {fname}"

    # LC02 – LC14 have .gitkeep
    for n in range(2, 15):
        lc = ssot / f"LC{n:02d}"
        assert lc.is_dir()
        assert (lc / ".gitkeep").is_file()

    # PUB / CSDB
    pub = sec / "PUB"
    assert (pub / "README.md").is_file()
    csdb = pub / "CSDB"
    assert (csdb / "README.md").is_file()
    for sd in CSDB_SUBDIRS:
        ietp = csdb / sd / "EXPORT" / "IETP"
        assert ietp.is_dir(), f"Missing CSDB sub-dir: {sd}"
        assert (ietp / ".gitkeep").is_file()


def test_technology_subaxis_directories(tmp_path: Path) -> None:
    """T-TECHNOLOGIES sub-axes must each have a directory with README."""
    root = tmp_path / "scaffold"
    build_scaffold(root)
    t_path = root / "T-TECHNOLOGIES"
    for subaxis in TAXONOMY["T-TECHNOLOGIES"]:
        sa_dir = t_path / subaxis
        assert sa_dir.is_dir(), f"Missing sub-axis dir: {subaxis}"
        assert (sa_dir / "README.md").is_file()


def test_propulsion_chapters(tmp_path: Path) -> None:
    """T-P sub-axis must contain CH70–CH77."""
    root = tmp_path / "scaffold"
    build_scaffold(root)
    prop = root / "T-TECHNOLOGIES" / "P-PROPULSION"
    ch_dirs = sorted(d.name for d in prop.iterdir() if d.is_dir())
    ch_codes = [d.split("-")[0] for d in ch_dirs]
    for code in ["CH70", "CH71", "CH72", "CH73", "CH74", "CH75", "CH76", "CH77"]:
        assert code in ch_codes, f"Missing propulsion chapter {code}"


def test_idempotent_rebuild(tmp_path: Path) -> None:
    """Running the builder twice must not raise or corrupt."""
    root = tmp_path / "scaffold"
    s1 = build_scaffold(root)
    s2 = build_scaffold(root)
    assert s1["chapters"] == s2["chapters"]
    assert s1["sections"] == s2["sections"]
