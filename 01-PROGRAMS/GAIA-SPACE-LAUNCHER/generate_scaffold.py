#!/usr/bin/env python3
"""GAIA-SL1 OPT-IN 5-Axis Scaffold Generator (GSL-TX-1.0).

Generates the full directory/file scaffold for the GAIA Space Launcher
programme, adapted from the canonical AMPEL360 topology to the OPT-IN
5-axis structure.

Axes
----
O  – Operations
P  – Programme
T  – Technologies  (7 sub-axes: S, P, F, E, A, C, TH)
I  – Integration
N  – Norms

Usage
-----
    python generate_scaffold.py              # writes to ./GAIA-SL1-SCAFFOLD
    python generate_scaffold.py -o /tmp/out  # custom output directory
    python generate_scaffold.py --dry-run    # print stats without writing

Edit the ``TAXONOMY`` dict below and re-execute to extend or modify.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Dict, List, Tuple

# ---------------------------------------------------------------------------
# Taxonomy definition – edit this dict to extend/modify the scaffold
# ---------------------------------------------------------------------------

# Each axis maps to a list of sub-axes.  For axes without sub-axes the list
# contains a single entry with key ``None``.  Each sub-axis maps to a list
# of (chapter_code, chapter_title, [section_titles]) tuples.

Axis = str
SubAxis = str | None
Chapter = Tuple[str, str, List[str]]

TAXONOMY: Dict[Axis, Dict[SubAxis, List[Chapter]]] = {
    # ------------------------------------------------------------------
    # O – OPERATIONS
    # ------------------------------------------------------------------
    "O-OPERATIONS": {
        None: [
            ("CH01", "Launch Operations", [
                "01-Pre-Launch Processing",
                "02-Launch Countdown",
                "03-Pad Operations",
                "04-Abort Procedures",
                "05-Post-Launch Safing",
                "06-Launch Window Analysis",
                "07-Ops Documentation",
            ]),
            ("CH02", "Mission Control", [
                "01-Flight Dynamics",
                "02-Telemetry Monitoring",
                "03-Command & Control",
                "04-Anomaly Resolution",
                "05-Mission Planning",
                "06-Orbit Determination",
                "07-End-of-Mission Ops",
            ]),
            ("CH03", "Ground Support Equipment", [
                "01-Mechanical GSE",
                "02-Electrical GSE",
                "03-Fluid GSE",
                "04-Transporter-Erector",
                "05-Umbilical Systems",
                "06-GSE Maintenance",
                "07-GSE Qualification",
            ]),
            ("CH04", "Recovery & Refurbishment", [
                "01-Booster Recovery",
                "02-Fairing Recovery",
                "03-Inspection & Assessment",
                "04-Refurbishment Procedures",
                "05-Reuse Certification",
                "06-Logistics & Transport",
            ]),
            ("CH05", "Spaceport Facilities", [
                "01-Launch Complex",
                "02-Integration Building",
                "03-Propellant Plant",
                "04-Control Centre",
                "05-Payload Processing Facility",
                "06-Infrastructure Maintenance",
            ]),
            ("CH06", "Range Safety", [
                "01-Flight Safety Systems",
                "02-Tracking & Surveillance",
                "03-Exclusion Zone Management",
                "04-Destruct Systems",
                "05-Range Coordination",
                "06-Safety Analysis & FHA",
            ]),
            ("CH07", "Propellant Operations", [
                "01-LOX Production & Storage",
                "02-LCH4 Production & Storage",
                "03-Propellant Transfer",
                "04-Cryogenic Handling",
                "05-Propellant Quality",
                "06-Spill & Vent Management",
                "07-Propellant Logistics",
            ]),
            ("CH08", "Payload Processing", [
                "01-Payload Receiving",
                "02-Cleanroom Operations",
                "03-Encapsulation",
                "04-Payload–Vehicle Mating",
                "05-Payload Checkout",
                "06-Hazardous Operations",
            ]),
            ("CH09", "Countdown & Sequencing", [
                "01-Terminal Count Sequence",
                "02-Automated Countdown",
                "03-Hold & Recycle",
                "04-Engine Start Sequence",
                "05-Liftoff Commit Criteria",
                "06-Ascent Sequencing",
            ]),
        ],
    },

    # ------------------------------------------------------------------
    # P – PROGRAMME
    # ------------------------------------------------------------------
    "P-PROGRAMME": {
        None: [
            ("CH10", "Programme Management", [
                "01-WBS & SOW",
                "02-Governance",
                "03-Stakeholder Management",
                "04-Reporting & Dashboards",
                "05-Reviews & Milestones",
                "06-Lessons Learned",
                "07-Programme Closure",
            ]),
            ("CH11", "Configuration Management", [
                "01-Configuration Identification",
                "02-Change Control",
                "03-Configuration Status Accounting",
                "04-Configuration Audits",
                "05-Baseline Management",
                "06-COTS/MOTS Tracking",
                "07-Digital Thread CM",
            ]),
            ("CH12", "Quality Assurance", [
                "01-Quality Planning",
                "02-Process Audits",
                "03-Non-Conformance Management",
                "04-Supplier Quality",
                "05-Metrology & Calibration",
                "06-Quality Records",
            ]),
            ("CH13", "Safety & Mission Assurance", [
                "01-System Safety",
                "02-Reliability Engineering",
                "03-FMECA",
                "04-Fault Tree Analysis",
                "05-Parts & Materials",
                "06-Contamination Control",
                "07-SMA Reviews",
            ]),
            ("CH14", "Procurement & Supply Chain", [
                "01-Make-or-Buy",
                "02-Supplier Selection",
                "03-Contract Management",
                "04-Incoming Inspection",
                "05-Inventory Management",
                "06-SCM Risk Mitigation",
            ]),
            ("CH15", "Cost Engineering", [
                "01-Cost Estimation",
                "02-Earned Value Management",
                "03-Budget Tracking",
                "04-Cost-at-Completion",
                "05-Parametric Models",
                "06-Cost Reduction Initiatives",
            ]),
            ("CH16", "Schedule & Planning", [
                "01-Master Schedule",
                "02-Critical Path Analysis",
                "03-Resource Loading",
                "04-Schedule Risk Assessment",
                "05-Integrated Planning",
                "06-Milestone Tracking",
            ]),
            ("CH17", "Risk Management", [
                "01-Risk Identification",
                "02-Risk Assessment",
                "03-Mitigation Planning",
                "04-Risk Register",
                "05-Opportunity Management",
                "06-Risk Reporting",
            ]),
        ],
    },

    # ------------------------------------------------------------------
    # T – TECHNOLOGIES  (7 sub-axes)
    # ------------------------------------------------------------------
    "T-TECHNOLOGIES": {
        # T-S  Structures
        "S-STRUCTURES": [
            ("CH50", "General Structures", [
                "01-Structural Design Criteria",
                "02-Materials Selection",
                "03-Structural Analysis",
                "04-Manufacturing Processes",
                "05-NDI & Inspection",
                "06-Structural Testing",
                "07-Damage Tolerance",
            ]),
            ("CH51", "First Stage Structure", [
                "01-Tank Section",
                "02-Intertank Structure",
                "03-Thrust Structure",
                "04-Aft Skirt",
                "05-Grid Fins",
                "06-Aerodynamic Surfaces",
                "07-First Stage Integration",
            ]),
            ("CH52", "Second Stage Structure", [
                "01-Upper Tank",
                "02-Common Bulkhead",
                "03-Aft Dome & Mounting",
                "04-Equipment Bay",
                "05-Payload Adapter",
                "06-Stage Separation System",
                "07-Second Stage Integration",
            ]),
            ("CH53", "Third Stage Structure (Q-ION)", [
                "01-Bus Structure",
                "02-Propellant Tanks",
                "03-Solar Array Mounting",
                "04-Antenna Structure",
                "05-Payload Interface Ring",
                "06-Third Stage Integration",
            ]),
            ("CH54", "Payload Fairing", [
                "01-Fairing Shell",
                "02-Acoustic Attenuation",
                "03-Separation Mechanism",
                "04-Access Doors & Venting",
                "05-Fairing Recovery System",
                "06-Fairing Qualification",
            ]),
            ("CH55", "Interstage & Landing Systems", [
                "01-Interstage Adapter",
                "02-Stage Separation Mechanism",
                "03-Landing Legs",
                "04-Crush Core & Shock Absorbers",
                "05-Leg Deployment Mechanism",
                "06-Landing Sensors & Radar",
                "07-Landing Gear Qualification",
            ]),
        ],
        # T-P  Propulsion
        "P-PROPULSION": [
            ("CH70", "Propulsion General", [
                "01-Propulsion Architecture",
                "02-Performance Requirements",
                "03-Engine Interfaces",
                "04-Propulsion Safety",
                "05-Propulsion Test Strategy",
                "06-Engine Life Management",
            ]),
            ("CH71", "RAPTOR-Q Main Engines (×9)", [
                "01-Combustion Chamber",
                "02-Turbopumps",
                "03-Injector Assembly",
                "04-Ignition System",
                "05-Regen Cooling",
                "06-Engine Controller",
                "07-Acceptance Testing",
                "08-Engine Reuse Protocol",
            ]),
            ("CH72", "RAPTOR-Q Vacuum Engine", [
                "01-Extended Nozzle",
                "02-Vacuum Performance",
                "03-Gimbal Assembly",
                "04-Thermal Management",
                "05-Altitude Start",
                "06-Engine Health Monitoring",
                "07-Vacuum Engine Qualification",
            ]),
            ("CH73", "Q-ION Drive", [
                "01-Ion Thruster Assembly",
                "02-Quantum Enhancement Module",
                "03-Propellant Feed (Xenon/Krypton)",
                "04-Power Processing Unit",
                "05-Beam Optics",
                "06-Long-Duration Operation",
                "07-Q-ION Qualification",
            ]),
            ("CH74", "Reaction Control System", [
                "01-RCS Thrusters",
                "02-Propellant Supply",
                "03-Valve Assemblies",
                "04-RCS Controller",
                "05-Attitude Authority",
                "06-RCS Qualification",
            ]),
            ("CH75", "FADEC – Engine Control", [
                "01-FADEC Architecture",
                "02-Sensor Suite",
                "03-Control Algorithms",
                "04-Redundancy Management",
                "05-FADEC Software V&V",
                "06-FADEC Qualification",
            ]),
            ("CH76", "Thrust Vector Control", [
                "01-TVC Actuators",
                "02-Gimbal Bearings",
                "03-Hydraulic/Electric Drive",
                "04-TVC Controller",
                "05-Slew Rate & Authority",
                "06-TVC Qualification",
            ]),
            ("CH77", "Propulsion Health Monitoring", [
                "01-Sensor Instrumentation",
                "02-Real-Time Diagnostics",
                "03-Anomaly Detection",
                "04-Predictive Analytics",
                "05-Data Recording",
                "06-PHM Qualification",
            ]),
        ],
        # T-F  Fluids
        "F-FLUIDS": [
            ("CH28", "Propellant Storage & Feed", [
                "01-LOX Tank Design",
                "02-LCH4 Tank Design",
                "03-Tank Pressurization",
                "04-Feed Lines & Bellows",
                "05-Anti-Vortex & Anti-Slosh",
                "06-Propellant Management Device",
                "07-Feed System Qualification",
            ]),
            ("CH29", "Pressurization Systems", [
                "01-Helium Pressurant",
                "02-Autogenous Pressurization",
                "03-COPV Tanks",
                "04-Regulators & Valves",
                "05-Pressure Control Logic",
                "06-Pressurization Qualification",
            ]),
            ("CH35", "Hydraulic Systems", [
                "01-Hydraulic Power Unit",
                "02-Accumulators",
                "03-Distribution Lines",
                "04-Actuator Interfaces",
                "05-Fluid & Filtration",
                "06-Hydraulic Qualification",
            ]),
        ],
        # T-E  Electrical
        "E-ELECTRICAL": [
            ("CH24", "Electrical Power System", [
                "01-Battery System",
                "02-Power Distribution",
                "03-Solar Array (Upper Stage)",
                "04-Power Conversion",
                "05-Harness & Cabling",
                "06-Grounding & Bonding",
                "07-EPS Qualification",
            ]),
            ("CH33", "Lighting & External Power", [
                "01-External Lighting",
                "02-Internal Lighting",
                "03-Ground Power Interface",
                "04-Umbilical Power",
                "05-Emergency Power",
                "06-Lighting Qualification",
            ]),
        ],
        # T-A  Avionics / GNC
        "A-AVIONICS-GNC": [
            ("CH22", "Auto-Flight / GNC", [
                "01-Navigation Sensors",
                "02-Guidance Algorithms",
                "03-Flight Control Laws",
                "04-IMU & Star Tracker",
                "05-GPS/GNSS Receiver",
                "06-GNC Software V&V",
                "07-GNC Qualification",
            ]),
            ("CH31", "Instruments & Displays", [
                "01-Vehicle Instrumentation",
                "02-Ground Display System",
                "03-Telemetry Formatting",
                "04-Data Acquisition",
                "05-Instrumentation Calibration",
                "06-Instrumentation Qualification",
            ]),
            ("CH34", "Quantum Flight Computer (QFC)", [
                "01-QFC Architecture",
                "02-Qubit Processor Interface",
                "03-Flight Software",
                "04-Redundancy & Voting",
                "05-Trajectory Optimiser",
                "06-Autonomous Decision Engine",
                "07-QFC Qualification",
            ]),
            ("CH42", "Autonomous Flight Termination (AFTS)", [
                "01-AFTS Architecture",
                "02-Independent Tracking",
                "03-Rule-Based Logic",
                "04-Safe & Arm Device",
                "05-AFTS Software V&V",
                "06-AFTS Qualification",
            ]),
        ],
        # T-C  Communications
        "C-COMMS": [
            ("CH23", "Communications Systems", [
                "01-S-Band Telemetry",
                "02-C-Band Tracking",
                "03-Payload Data Relay",
                "04-Range Safety Comms",
                "05-Inter-Stage Link",
                "06-Encryption & Security",
                "07-Comms Qualification",
            ]),
        ],
        # T-TH  Thermal / TPS
        "TH-THERMAL-TPS": [
            ("CH21", "Thermal Protection System", [
                "01-TPS Materials",
                "02-Heatshield Design",
                "03-Re-Entry Thermal Analysis",
                "04-Ablative Protection",
                "05-TPS Bonding & Attachment",
                "06-TPS Inspection & Repair",
                "07-TPS Qualification",
            ]),
            ("CH26", "Fire Protection & Thermal Control", [
                "01-Fire Detection",
                "02-Fire Suppression",
                "03-Thermal Insulation",
                "04-Active Thermal Control",
                "05-Cryogenic Insulation",
                "06-Thermal Control Qualification",
            ]),
        ],
    },

    # ------------------------------------------------------------------
    # I – INTEGRATION
    # ------------------------------------------------------------------
    "I-INTEGRATION": {
        None: [
            ("CH80", "System Integration", [
                "01-Integration Planning",
                "02-Interface Control",
                "03-Functional Integration",
                "04-Combined Systems Test",
                "05-Electromagnetic Compatibility",
                "06-Mass Properties",
                "07-System Integration Review",
            ]),
            ("CH81", "Vehicle Assembly", [
                "01-Stage Assembly",
                "02-Engine Installation",
                "03-Avionics Installation",
                "04-Harness & Plumbing",
                "05-Closeout & Inspection",
                "06-Assembly Verification",
                "07-Assembly Records",
            ]),
            ("CH82", "Software & Avionics Integration", [
                "01-SW Load & Configuration",
                "02-Avionics Functional Test",
                "03-Hardware-in-Loop Simulation",
                "04-End-to-End Data Flow",
                "05-SW/HW Interface Verification",
                "06-Avionics Integration Review",
            ]),
            ("CH83", "Payload Integration", [
                "01-Payload Interface Verification",
                "02-Payload Mating",
                "03-Combined Electrical Test",
                "04-Payload Fairing Encapsulation",
                "05-Integrated Payload Checkout",
                "06-Payload Integration Review",
            ]),
            ("CH84", "Launch Readiness Review", [
                "01-LRR Criteria",
                "02-Open-Work Closeout",
                "03-Waivers & Deviations",
                "04-Flight Rationale",
                "05-Go/No-Go Polling",
                "06-LRR Documentation",
            ]),
            ("CH85", "Test & Evaluation", [
                "01-Static Fire Test",
                "02-Structural Qualification",
                "03-Vibration & Acoustic Test",
                "04-Thermal Vacuum Test",
                "05-Separation & Deployment Test",
                "06-Flight Test Campaign",
                "07-Test Reporting",
            ]),
        ],
    },

    # ------------------------------------------------------------------
    # N – NORMS
    # ------------------------------------------------------------------
    "N-NORMS": {
        None: [
            ("CH90", "Certification & Compliance", [
                "01-Launch Licence",
                "02-FAA/AST Compliance",
                "03-ESA Requirements (ECSS)",
                "04-NASA Standards (NASA-STD)",
                "05-National Regulations",
                "06-Compliance Matrix",
            ]),
            ("CH91", "Environmental & Sustainability", [
                "01-Environmental Impact Assessment",
                "02-Noise & Emissions",
                "03-Space Debris Mitigation",
                "04-Deorbit & Passivation",
                "05-Sustainability Reporting",
            ]),
            ("CH92", "Export Control & ITAR", [
                "01-ITAR Classification",
                "02-EAR Classification",
                "03-Technology Transfer",
                "04-Export Licences",
            ]),
        ],
    },
}

# ---------------------------------------------------------------------------
# Canonical per-section structure
# ---------------------------------------------------------------------------

LIFECYCLE_CODES = [f"LC{n:02d}" for n in range(1, 15)]

LC01_TEMPLATES: List[Tuple[str, str]] = [
    ("KNOTS.csv", "knot_id,title,description,status,owner,due_date\n"),
    ("KNU_PLAN.csv", "knu_id,knowledge_unit,plan_ref,milestone,status\n"),
    ("TIMELINE.csv", "event_id,event,start_date,end_date,milestone,dependency\n"),
    ("RACI.csv", "activity,responsible,accountable,consulted,informed\n"),
    (
        "TOKENOMICS_TT.yaml",
        (
            "# Tokenomics Twin-Token template\n"
            "token_id: ~\n"
            "section: ~\n"
            "allocation: 0\n"
            "vesting_schedule: ~\n"
        ),
    ),
    ("AWARDS_TT.csv", "award_id,recipient,category,date,description\n"),
]

CSDB_SUBDIRS = ["DM", "PM", "DML", "BREX", "ICN", "COMMON", "APPLICABILITY"]

# ---------------------------------------------------------------------------
# README content generators
# ---------------------------------------------------------------------------


def _axis_readme(axis: str) -> str:
    return (
        f"# {axis}\n\n"
        f"OPT-IN axis **{axis.split('-')[0]}** – "
        f"{axis.split('-', 1)[1].replace('-', ' ').title()}\n\n"
        f"Part of the GAIA-SL1 OPT-IN 5-Axis Scaffold (GSL-TX-1.0).\n"
    )


def _subaxis_readme(axis: str, subaxis: str) -> str:
    return (
        f"# {axis} / {subaxis}\n\n"
        f"Sub-axis **{subaxis.split('-')[0]}** – "
        f"{subaxis.split('-', 1)[1].replace('-', ' ').title()}\n\n"
        f"Technology sub-axis under {axis}.\n"
    )


def _chapter_readme(chapter_code: str, chapter_title: str, path_ctx: str) -> str:
    return (
        f"# {chapter_code} – {chapter_title}\n\n"
        f"Chapter **{chapter_code}** of the GAIA-SL1 launcher scaffold.\n\n"
        f"Path: `{path_ctx}`\n"
    )


def _section_readme(
    chapter_code: str,
    chapter_title: str,
    section_title: str,
    path_ctx: str,
) -> str:
    return (
        f"# {chapter_code} / {section_title}\n\n"
        f"Section under **{chapter_code} – {chapter_title}**.\n\n"
        f"Path: `{path_ctx}`\n\n"
        "## Canonical Layout\n\n"
        "```\n"
        "SSOT/\n"
        "  LC01/  (templates: KNOTS, KNU_PLAN, TIMELINE, RACI, "
        "TOKENOMICS_TT, AWARDS_TT)\n"
        "  LC02 … LC14/\n"
        "PUB/\n"
        "  CSDB/\n"
        "    DM/ PM/ DML/ BREX/ ICN/ COMMON/ APPLICABILITY/\n"
        "      EXPORT/ IETP/\n"
        "```\n"
    )


def _ssot_readme(section_title: str) -> str:
    return (
        f"# SSOT – {section_title}\n\n"
        "Single Source of Truth for this section.\n\n"
        "Lifecycle directories LC01 – LC14 hold artefacts for each\n"
        "programme phase.\n"
    )


def _pub_readme(section_title: str) -> str:
    return (
        f"# PUB – {section_title}\n\n"
        "Publication module for this section.\n\n"
        "CSDB sub-directories follow S1000D conventions:\n"
        "DM, PM, DML, BREX, ICN, COMMON, APPLICABILITY.\n"
    )


# ---------------------------------------------------------------------------
# Scaffold builder
# ---------------------------------------------------------------------------


def build_scaffold(root: Path) -> dict:
    """Create the full GAIA-SL1 OPT-IN scaffold under *root*.

    Returns a dict with ``dirs``, ``files``, ``chapters``, ``sections``
    counts.
    """
    stats = {"dirs": 0, "files": 0, "chapters": 0, "sections": 0}

    def _mkdir(p: Path) -> None:
        p.mkdir(parents=True, exist_ok=True)
        stats["dirs"] += 1

    def _write(p: Path, content: str) -> None:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        stats["files"] += 1

    # Root README
    _write(
        root / "README.md",
        "# GAIA-SL1 OPT-IN Scaffold\n\n"
        "Auto-generated OPT-IN 5-axis topology for the GAIA Space Launcher.\n\n"
        "Taxonomy version: **GSL-TX-1.0**\n",
    )

    for axis, subaxes in TAXONOMY.items():
        axis_path = root / axis
        _write(axis_path / "README.md", _axis_readme(axis))

        for subaxis, chapters in subaxes.items():
            if subaxis is not None:
                sa_path = axis_path / subaxis
                _write(sa_path / "README.md", _subaxis_readme(axis, subaxis))
            else:
                sa_path = axis_path

            for ch_code, ch_title, sections in chapters:
                stats["chapters"] += 1
                ch_path = sa_path / f"{ch_code}-{ch_title.replace(' ', '_')}"
                ch_ctx = str(ch_path.relative_to(root))
                _write(
                    ch_path / "README.md",
                    _chapter_readme(ch_code, ch_title, ch_ctx),
                )

                for sec_title in sections:
                    stats["sections"] += 1
                    sec_path = ch_path / sec_title.replace(" ", "_")
                    sec_ctx = str(sec_path.relative_to(root))
                    _write(
                        sec_path / "README.md",
                        _section_readme(ch_code, ch_title, sec_title, sec_ctx),
                    )

                    # --- SSOT ---
                    ssot = sec_path / "SSOT"
                    _write(ssot / "README.md", _ssot_readme(sec_title))
                    for lc in LIFECYCLE_CODES:
                        lc_dir = ssot / lc
                        _mkdir(lc_dir)
                        if lc == "LC01":
                            for fname, content in LC01_TEMPLATES:
                                _write(lc_dir / fname, content)
                        else:
                            _write(lc_dir / ".gitkeep", "")

                    # --- PUB / CSDB ---
                    pub = sec_path / "PUB"
                    _write(pub / "README.md", _pub_readme(sec_title))
                    csdb = pub / "CSDB"
                    _write(csdb / "README.md", "# CSDB\n\nCommon Source DataBase.\n")
                    for sd in CSDB_SUBDIRS:
                        ietp = csdb / sd / "EXPORT" / "IETP"
                        _mkdir(ietp)
                        _write(ietp / ".gitkeep", "")

    return stats


# ---------------------------------------------------------------------------
# Taxonomy summary (for dry-run / reporting)
# ---------------------------------------------------------------------------


def taxonomy_summary() -> dict:
    """Return chapter/section counts without writing anything."""
    chapters = 0
    sections = 0
    for _axis, subaxes in TAXONOMY.items():
        for _sa, chaps in subaxes.items():
            for _code, _title, secs in chaps:
                chapters += 1
                sections += len(secs)
    return {"chapters": chapters, "sections": sections}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Generate GAIA-SL1 OPT-IN 5-axis scaffold."
    )
    parser.add_argument(
        "-o",
        "--output",
        default="GAIA-SL1-SCAFFOLD",
        help="Output root directory (default: ./GAIA-SL1-SCAFFOLD)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print taxonomy stats without writing files.",
    )
    args = parser.parse_args(argv)

    if args.dry_run:
        s = taxonomy_summary()
        print(
            f"Taxonomy GSL-TX-1.0: {s['chapters']} chapters, "
            f"{s['sections']} sections"
        )
        return

    root = Path(args.output)
    stats = build_scaffold(root)
    print(
        f"Scaffold created at {root.resolve()}\n"
        f"  {stats['dirs']:,} directories\n"
        f"  {stats['files']:,} files\n"
        f"  {stats['chapters']} chapters\n"
        f"  {stats['sections']} sections"
    )


if __name__ == "__main__":
    main()
