# Elastic Governance Layer (EGL)

## A Composite Public Law Control Matrix for AI-Assisted Decision-Making

**Elastic Governance Layer (EGL)** is an open governance specification for preventing **premature institutional closure** in AI-assisted decision-making.

EGL is designed for public authorities, regulated institutions, legal and compliance teams, auditors, procurement officials, system designers, and researchers working with consequential AI-assisted pathways.

> **No consequential institutional pathway should be treated as lawfully closed unless the relevant justificatory, participatory, corrective, and anti-fettering controls have been activated, proportionately applied, and institutionally evidenced.**

---

## What Problem Does EGL Solve?

AI-assisted systems increasingly classify information, assign risk, route cases, recommend outcomes, generate reasons, and influence institutional decisions.

The central governance risk is not limited to hallucination, bias, inaccuracy, or fully automated decision-making. A pathway may become practically fixed before lawful institutional judgment occurs:

- a classification may become difficult to challenge;
- a score may determine the procedural route;
- a recommendation may become the default outcome;
- generated reasons may conceal earlier pathway closure;
- nominal human review may merely confirm a machine-shaped result.

EGL defines this condition as **premature institutional closure**.

---

## Formal Definition

> **The Elastic Governance Layer is the fourth control layer within Closure-Gated AI Governance. It operates as a composite public-law matrix that keeps AI-generated classifications, predictions, recommendations, and reasons provisional, contestable, reviewable, and returnable until lawful human and institutional closure is achieved.**

“Elastic” does not mean unrestricted managerial flexibility. It refers to the legally governed capacity of an institutional pathway to remain revisable before consequence.

---

## The EGL Composite Public Law Control Matrix

EGL contains four interdependent control dimensions:

| Control Dimension | Core Function |
|---|---|
| **Justificatory Control** | Requires lawful authority, rational connection, alternatives, necessity, and proportionate justification |
| **Participatory Control** | Preserves meaningful notice, disclosure, response, factual correction, and contestability |
| **Corrective Control** | Preserves traceability, review, reopening, return, correction, and practical remedy |
| **Anti-Fettering Control** | Preserves genuine human discretion and prevents scores, templates, classifications, or recommendations from becoming de facto final decisions |

These controls operate across the institutional pathway:

```text
Input → Classification → Routing → Recommendation → Decision → Reasons → Review
```

EGL is therefore both:

- **vertical**, as the fourth layer within the broader architecture; and
- **horizontal**, as a control matrix operating across the full decision pathway.

---

## Position within Closure-Gated AI Governance

```text
PJLS → CDM → 4-3-3-2 → EGL → GTL / Human Closure
```

| Layer | Core Question | Primary Function |
|---|---|---|
| **PJLS** | What may enter the system? | Evidence and authority admission |
| **CDM** | Where does the matter belong? | Institutional classification and separation |
| **4-3-3-2** | How should the route be structured? | Legal coding and institutional routing |
| **EGL** | What must remain open before consequence? | Public-law control against premature closure |
| **GTL / Human Closure** | What may be transmitted, and who may finalize it? | Controlled transmission and lawful institutional closure |

EGL does not replace the surrounding layers. Its specific role is to govern the space between structured machine output and lawful consequential closure.

---

## Pathway States

An EGL-governed pathway may occupy the following states:

```text
OPEN
PAUSED
RETURNED
REOPENED
ESCALATED
RESTRICTED
READY_FOR_TRANSMISSION
LAWFULLY_CLOSED
```

A pathway must not advance merely because technical processing is complete.

Progression requires an explicit closure-gate outcome supported by lawful authority, relevant controls, and institutional evidence.

---

## Risk-Based Application

### Low Impact

Typical requirements include:

- basic traceability;
- accessible correction;
- a clear distinction between provisional and final output;
- basic human review.

### Medium Impact

Typical requirements include:

- formal pathway mapping;
- meaningful participation;
- independent human review;
- structured reasons;
- pause, return, and escalation functions.

### High Impact

Typical requirements include:

- complete coverage of all four EGL dimensions;
- node-specific controls at every material closure point;
- genuine human authority to reopen the pathway;
- a full review-ready institutional record;
- independent and recurring assurance.

---

## EGL Maturity Model

| Level | Maturity State |
|---|---|
| **Level 0** | Uncontrolled Automation |
| **Level 1** | Nominal Human Review |
| **Level 2** | Traceable Assistance |
| **Level 3** | EGL-Controlled Institutional Pathway |
| **Level 4** | Review-Ready Institutional Closure |

The maturity level is determined by the institution’s demonstrated governance capacity, not by the sophistication of the AI model.

---

## Repository Structure

```text
elastic-governance-layer/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── GOVERNANCE.md
│
├── white-paper/
├── specification/
├── annex/
├── schemas/
├── domain-profiles/
└── examples/
```

Planned components include:

- the EGL White Paper;
- core definitions;
- the Composite Public Law Control Matrix;
- the Pathway-Control Matrix;
- closure-gate and pathway-state specifications;
- risk classification;
- the Institutional Evidence Register;
- the EGL Maturity Model;
- implementation checklists;
- domain profiles;
- machine-readable schemas;
- reference examples.

---

## Initial Application Domains

The first EGL domain profiles are expected to address:

- public administration and benefits;
- tax administration and enforcement;
- regulatory investigation and enforcement;
- education administration;
- regulated financial decision-making;
- cross-jurisdictional smart justice.

---

## Status and Versioning

**Current version:** `v0.2.0 — Control, Pathway, and Closure-Gate Specification`

Version 0.2 moves EGL from a concept and white-paper specification into an initial operational specification.

This release adds:

- a normative four-control gate procedure;
- explicit pathway-state and transition rules;
- a Python reference implementation;
- a machine-readable JSON Schema;
- a tax-administration reference example;
- a defined relationship between EGL, GTL, and lawful human closure.

```text
v0.1 — Concept and White Paper Specification
v0.2 — Control, Pathway, and Closure-Gate Specification [CURRENT]
v0.3 — Institutional Evidence and Human Judgment Record
v0.4 — Domain Profiles and Implementation Templates
v0.5 — Extended Reference Implementation and Testing
v1.0 — First Stable Public Specification
```

Version 0.2 extends rather than replaces version 0.1. The original public development record remains preserved.

## Citation

Formal citation metadata is provided in [`CITATION.cff`](CITATION.cff).

For the current operational specification, cite:

> Huang, Jim Y. *The Elastic Governance Layer: Control, Pathway, and Closure-Gate Specification*. Version 0.2.0, 2026. https://github.com/jimyongzhihuang/Elastic-Governance-Layer

The original conceptual and white-paper specification remains citable as Version 0.1.

---

## Author

**Jim Y. Huang**  
University of Toronto, OISE

---

## Scope and Non-Substitution

EGL is a governance specification and reference architecture. It does not replace lawful authority, substantive legal analysis, judicial or administrative review, procedural fairness, privacy and data governance, equality law, technical validation, cybersecurity, professional responsibility, or sector-specific regulation.

EGL does not promise error-free automation. Its purpose is to keep machine-assisted institutional pathways open to justification, participation, correction, review, and genuine human judgment until lawful closure is achieved.

---

## Development Status

This repository is under active development.

### Completed in Version 0.2

- publication of the normative EGL control algorithm;
- release of the pathway-state and closure-gate logic;
- release of the Python reference implementation;
- release of the machine-readable pathway schema;
- publication of the first tax-administration reference example;
- integration of EGL with the wider PJLS, CDM, 4-3-3-2, GTL, and human-closure architecture.

### Next Development Priorities

1. institutional evidence and human judgment record schemas;
2. automated validation tests for the Python implementation and JSON Schema;
3. additional domain profiles for public administration, education, regulation, finance, and smart justice;
4. implementation and procurement templates;
5. preparation of a tagged Version 0.2 release.

---

## Licence

Licence terms will be added in the repository’s `LICENSE` file.
