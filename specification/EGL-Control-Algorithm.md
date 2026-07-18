# EGL Control Algorithm

## Version 0.2.0 — Control, Pathway, and Closure-Gate Specification

## 1. Purpose

This specification converts the Elastic Governance Layer (EGL) from a conceptual public-law matrix into an auditable pathway-control procedure.

EGL governs the interval between structured machine output and lawful institutional consequence. It determines whether an AI-assisted pathway may advance, must remain provisional, or must be paused, returned, reopened, escalated, or restricted before human or institutional closure.

EGL does not decide the substantive legal merits of a matter. It controls whether the institutional pathway has satisfied the conditions necessary to move toward consequence.

## 2. Governing Principle

> No consequential institutional pathway should be treated as lawfully closed unless the relevant justificatory, participatory, corrective, and anti-fettering controls have been activated, proportionately applied, institutionally evidenced, and completed through authorized human or institutional judgment.

Technical completion is not lawful institutional closure.

## 3. Required Pathway Inputs

Each material pathway node MUST identify:

- the institutional pathway and node;
- the proposed output and consequence;
- the applicable authority basis;
- the responsibility boundary;
- the admitted evidence record;
- the applicable risk tier;
- the responsible human reviewer;
- the four EGL control assessments;
- the institutional evidence supporting those assessments.

An absent required input is not treated as a negative decision on the substantive merits. It is a governance defect that prevents pathway advancement.

## 4. Four-Control Assessment

At every material closure point, the pathway MUST assess:

1. **Justificatory Control** — lawful authority, rational connection, relevant alternatives, necessity, proportionality, and intelligible reasons.
2. **Participatory Control** — notice, disclosure, meaningful opportunity to respond, factual correction, and contestability.
3. **Corrective Control** — traceability, return, reopening, review, correction, and practical remedy.
4. **Anti-Fettering Control** — genuine human authority to depart from machine-generated classifications, scores, templates, recommendations, or reasons.

Each control receives one status:

```text
SATISFIED
PARTIAL
FAILED
NOT_APPLICABLE
```

A `NOT_APPLICABLE` finding MUST include a recorded legal or institutional justification.

## 5. EGL Gate Procedure

```text
function EGL_GATE(pathway):

    validate required pathway inputs

    if a required input is missing:
        return PAUSED with remediation requirements

    identify the risk tier and material closure point

    assess:
        justificatory control
        participatory control
        corrective control
        anti-fettering control

    verify institutional evidence for each assessment

    if lawful authority is absent:
        return RESTRICTED

    if the responsibility boundary is unresolved:
        return RESTRICTED

    if required participation has not been meaningfully completed:
        return RETURNED

    if material facts, classification, or routing remain disputed:
        return ESCALATED

    if correction, review, or reopening is unavailable:
        return PAUSED

    if the human reviewer cannot practically depart from machine output:
        return RESTRICTED

    if any mandatory control is FAILED:
        return RETURNED, ESCALATED, or RESTRICTED

    if any mandatory control is PARTIAL:
        return PAUSED or RETURNED

    if all mandatory controls are SATISFIED
    and institutional evidence is complete:
        return READY_FOR_TRANSMISSION

    lawful closure may occur only through an identified
    human or institutional actor acting within lawful authority
```

## 6. Pathway States

| State | Meaning |
|---|---|
| `OPEN` | Processing may continue, but consequential closure is not permitted. |
| `PAUSED` | Advancement is suspended pending specified evidence or control remediation. |
| `RETURNED` | The matter is sent to an earlier node for correction, participation, or reclassification. |
| `REOPENED` | A previously advanced or closed pathway is restored for lawful reconsideration. |
| `ESCALATED` | The matter requires a reviewer with different authority, independence, or expertise. |
| `RESTRICTED` | The proposed use or consequence is prohibited under the present authority or control conditions. |
| `READY_FOR_TRANSMISSION` | EGL requirements are satisfied and GTL may govern the permitted output channel. |
| `LAWFULLY_CLOSED` | An authorized human or institution has completed and evidenced lawful closure. |

## 7. State-Transition Rules

- `OPEN` may move to `PAUSED`, `RETURNED`, `ESCALATED`, `RESTRICTED`, or `READY_FOR_TRANSMISSION`.
- `PAUSED` may return to `OPEN` only after the recorded defect is remediated.
- `RETURNED` MUST identify the destination node and reason for return.
- `ESCALATED` MUST identify the receiving authority and escalation basis.
- `READY_FOR_TRANSMISSION` may move toward `LAWFULLY_CLOSED` only through GTL and an accountable human closure record.
- `LAWFULLY_CLOSED` may move to `REOPENED` where review, appeal, correction, new evidence, or lawful reconsideration permits.

A pathway MUST NOT advance merely because technical processing is complete.

## 8. Relationship to the Wider Architecture

```text
PJLS → CDM → 4-3-3-2 → EGL → GTL → Human / Institutional Closure
```

- **PJLS** governs evidence and authority admission.
- **CDM** governs institutional classification and separation.
- **4-3-3-2** structures legal coding and institutional routing.
- **EGL** keeps the pathway provisional, contestable, correctable, and reviewable.
- **GTL** governs transmission into differentiated output channels.
- **Human or Institutional Closure** determines whether lawful consequence may finally arise.

Spring Governance explains the engineering behaviour of EGL through permitted movement, damping, and return-to-path. The Composite Public Law Control Matrix supplies the normative public-law conditions governing whether that movement may proceed toward institutional consequence.

## 9. Closure Rule

No consequential pathway is EGL-compliant merely because an AI system has produced a complete or technically valid answer.

Lawful closure requires:

- an identified and authorized institutional actor;
- satisfied mandatory EGL controls;
- a reviewable institutional evidence record;
- genuine human authority to accept, reject, revise, return, or reopen the machine-assisted pathway;
- a recorded legal and institutional basis for consequence.

## 10. Implementation References

This normative specification is accompanied by:

```text
reference-implementation/egl_gate.py
schemas/egl-pathway.schema.json
examples/tax-administration-example.json
```

These implementation materials demonstrate the EGL control logic. They do not replace applicable law, substantive legal analysis, professional judgment, procedural fairness, privacy and equality requirements, cybersecurity, technical validation, or judicial and administrative review.
