# Changelog

This file records the public development history of the Elastic Governance Layer (EGL).

Each release identifies its status, substantive additions, clarifications, compatibility position, and future development direction.

---

## Version History

### Version 0.2.0 — Control, Pathway, and Closure-Gate Specification

**Release date:** July 18, 2026  
**Status:** Initial Operational Specification

Version 0.2.0 moves EGL from a concept and white-paper specification into an initial operational governance specification.

#### Added

- normative EGL four-control gate procedure;
- explicit pathway states and state-transition rules;
- lawful closure requirements;
- Python reference control-gate implementation;
- machine-readable JSON pathway schema;
- tax-administration reference example;
- implementation links between EGL, GTL, and human or institutional closure.

#### Clarified

- technical completion is not lawful institutional closure;
- Spring Governance explains movement, damping, and return-to-path;
- the Composite Public Law Control Matrix supplies the normative public-law conditions for pathway advancement;
- EGL governs the interval between structured machine output and GTL-controlled transmission;
- lawful closure requires authorized human or institutional judgment.

#### Implementation Files

```text
specification/EGL-Control-Algorithm.md
reference-implementation/egl_gate.py
schemas/egl-pathway.schema.json
examples/tax-administration-example.json
