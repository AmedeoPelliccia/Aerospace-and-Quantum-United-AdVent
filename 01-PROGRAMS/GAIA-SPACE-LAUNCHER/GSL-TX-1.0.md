# GSL-TX-1.0 — GAIA-SL1 OPT-IN Taxonomy Mapping

> **Programme:** GAIA Space Launcher (GAIA-SL1)
> **Taxonomy version:** 1.0
> **Generator:** `generate_scaffold.py`
> **Totals:** 52 chapters · 333 sections · ~10 000 files

---

## OPT-IN 5-Axis Overview

| Axis | Code | Scope | Chapters |
|------|------|-------|----------|
| **Operations** | O | Launch ops, mission control, GSE, recovery, range safety | CH01 – CH09 |
| **Programme** | P | Mgmt, CM, QA, SMA, procurement, cost, schedule, risk | CH10 – CH17 |
| **Technologies** | T | Vehicle systems (7 sub-axes, see below) | CH21 – CH77 |
| **Integration** | I | System integration, assembly, SW, payload, LRR, T&E | CH80 – CH85 |
| **Norms** | N | Certification, environmental, export control | CH90 – CH92 |

---

## T – TECHNOLOGIES Sub-Axes

The Technologies axis maps the three-stage vehicle (RAPTOR-Q → H2-HYBRID → Q-ION)
plus cross-cutting disciplines to seven sub-axes:

| Sub-Axis | Code | Discipline | Chapters |
|----------|------|-----------|----------|
| **Structures** | S | Airframe, fairing, interstage, landing legs | CH50 – CH55 |
| **Propulsion** | P | RAPTOR-Q ×9, vacuum engine, Q-ION, RCS, FADEC, TVC, PHM | CH70 – CH77 |
| **Fluids** | F | Propellant storage/feed, pressurization, hydraulics | CH28, CH29, CH35 |
| **Electrical** | E | EPS, lighting & external power | CH24, CH33 |
| **Avionics / GNC** | A | GNC, instruments, QFC, AFTS | CH22, CH31, CH34, CH42 |
| **Communications** | C | S-band, C-band, payload relay, range safety comms | CH23 |
| **Thermal / TPS** | TH | Thermal protection, fire protection & thermal control | CH21, CH26 |

---

## Full Chapter / Section Index

### O – OPERATIONS

| Chapter | Title | Sections |
|---------|-------|----------|
| CH01 | Launch Operations | 7 |
| CH02 | Mission Control | 7 |
| CH03 | Ground Support Equipment | 7 |
| CH04 | Recovery & Refurbishment | 6 |
| CH05 | Spaceport Facilities | 6 |
| CH06 | Range Safety | 6 |
| CH07 | Propellant Operations | 7 |
| CH08 | Payload Processing | 6 |
| CH09 | Countdown & Sequencing | 6 |
| | **Subtotal** | **58** |

### P – PROGRAMME

| Chapter | Title | Sections |
|---------|-------|----------|
| CH10 | Programme Management | 7 |
| CH11 | Configuration Management | 7 |
| CH12 | Quality Assurance | 6 |
| CH13 | Safety & Mission Assurance | 7 |
| CH14 | Procurement & Supply Chain | 6 |
| CH15 | Cost Engineering | 6 |
| CH16 | Schedule & Planning | 6 |
| CH17 | Risk Management | 6 |
| | **Subtotal** | **51** |

### T – TECHNOLOGIES

#### T-S — Structures

| Chapter | Title | Sections |
|---------|-------|----------|
| CH50 | General Structures | 7 |
| CH51 | First Stage Structure | 7 |
| CH52 | Second Stage Structure | 7 |
| CH53 | Third Stage Structure (Q-ION) | 6 |
| CH54 | Payload Fairing | 6 |
| CH55 | Interstage & Landing Systems | 7 |
| | **Subtotal** | **40** |

#### T-P — Propulsion

| Chapter | Title | Sections |
|---------|-------|----------|
| CH70 | Propulsion General | 6 |
| CH71 | RAPTOR-Q Main Engines (×9) | 8 |
| CH72 | RAPTOR-Q Vacuum Engine | 7 |
| CH73 | Q-ION Drive | 7 |
| CH74 | Reaction Control System | 6 |
| CH75 | FADEC – Engine Control | 6 |
| CH76 | Thrust Vector Control | 6 |
| CH77 | Propulsion Health Monitoring | 6 |
| | **Subtotal** | **52** |

#### T-F — Fluids

| Chapter | Title | Sections |
|---------|-------|----------|
| CH28 | Propellant Storage & Feed | 7 |
| CH29 | Pressurization Systems | 6 |
| CH35 | Hydraulic Systems | 6 |
| | **Subtotal** | **19** |

#### T-E — Electrical

| Chapter | Title | Sections |
|---------|-------|----------|
| CH24 | Electrical Power System | 7 |
| CH33 | Lighting & External Power | 6 |
| | **Subtotal** | **13** |

#### T-A — Avionics / GNC

| Chapter | Title | Sections |
|---------|-------|----------|
| CH22 | Auto-Flight / GNC | 7 |
| CH31 | Instruments & Displays | 6 |
| CH34 | Quantum Flight Computer (QFC) | 7 |
| CH42 | Autonomous Flight Termination (AFTS) | 6 |
| | **Subtotal** | **26** |

#### T-C — Communications

| Chapter | Title | Sections |
|---------|-------|----------|
| CH23 | Communications Systems | 7 |
| | **Subtotal** | **7** |

#### T-TH — Thermal / TPS

| Chapter | Title | Sections |
|---------|-------|----------|
| CH21 | Thermal Protection System | 7 |
| CH26 | Fire Protection & Thermal Control | 6 |
| | **Subtotal** | **13** |

### I – INTEGRATION

| Chapter | Title | Sections |
|---------|-------|----------|
| CH80 | System Integration | 7 |
| CH81 | Vehicle Assembly | 7 |
| CH82 | Software & Avionics Integration | 6 |
| CH83 | Payload Integration | 6 |
| CH84 | Launch Readiness Review | 6 |
| CH85 | Test & Evaluation | 7 |
| | **Subtotal** | **39** |

### N – NORMS

| Chapter | Title | Sections |
|---------|-------|----------|
| CH90 | Certification & Compliance | 6 |
| CH91 | Environmental & Sustainability | 5 |
| CH92 | Export Control & ITAR | 4 |
| | **Subtotal** | **15** |

---

## Grand Totals

| Metric | Count |
|--------|-------|
| Axes | 5 |
| Sub-axes (T only) | 7 |
| Chapters | **52** |
| Sections | **333** |

---

## Per-Section Canonical Layout

Every section carries the same internal structure:

```
<section>/
├── README.md
├── SSOT/
│   ├── README.md
│   ├── LC01/          ← templates pre-populated
│   │   ├── KNOTS.csv
│   │   ├── KNU_PLAN.csv
│   │   ├── TIMELINE.csv
│   │   ├── RACI.csv
│   │   ├── TOKENOMICS_TT.yaml
│   │   └── AWARDS_TT.csv
│   ├── LC02/ … LC14/  ← empty (.gitkeep)
│   └── README.md
└── PUB/
    ├── README.md
    └── CSDB/
        ├── README.md
        ├── DM/EXPORT/IETP/
        ├── PM/EXPORT/IETP/
        ├── DML/EXPORT/IETP/
        ├── BREX/EXPORT/IETP/
        ├── ICN/EXPORT/IETP/
        ├── COMMON/EXPORT/IETP/
        └── APPLICABILITY/EXPORT/IETP/
```

**Lifecycle codes (LC01 – LC14):**

| Code | Phase |
|------|-------|
| LC01 | Concept |
| LC02 | Preliminary Design |
| LC03 | Detailed Design |
| LC04 | Manufacturing |
| LC05 | Assembly |
| LC06 | Integration |
| LC07 | Test & Qualification |
| LC08 | Certification |
| LC09 | Operations |
| LC10 | Maintenance |
| LC11 | Modification |
| LC12 | Repair |
| LC13 | Retirement |
| LC14 | Disposal |

---

*Generated by `generate_scaffold.py` — GSL-TX-1.0*
