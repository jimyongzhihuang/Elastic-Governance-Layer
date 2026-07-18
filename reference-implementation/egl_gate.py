"""
Elastic Governance Layer (EGL)
Reference Control-Gate Implementation

Version: 0.2.0
Author: Jim Y. Huang

This reference implementation demonstrates how an institutional
pathway may be paused, returned, escalated, restricted, or prepared
for transmission before lawful human or institutional closure.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class ControlStatus(str, Enum):
    SATISFIED = "SATISFIED"
    PARTIAL = "PARTIAL"
    FAILED = "FAILED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class PathwayState(str, Enum):
    OPEN = "OPEN"
    PAUSED = "PAUSED"
    RETURNED = "RETURNED"
    REOPENED = "REOPENED"
    ESCALATED = "ESCALATED"
    RESTRICTED = "RESTRICTED"
    READY_FOR_TRANSMISSION = "READY_FOR_TRANSMISSION"
    LAWFULLY_CLOSED = "LAWFULLY_CLOSED"


@dataclass
class ControlAssessment:
    status: ControlStatus
    evidence_refs: List[str] = field(default_factory=list)
    reason: str = ""


@dataclass
class EGLPathway:
    pathway_id: str
    node_id: str
    risk_tier: str
    authority_confirmed: bool
    responsibility_boundary_confirmed: bool
    participation_required: bool
    participation_completed: bool
    correction_available: bool
    human_override_available: bool
    material_dispute: bool
    controls: Dict[str, ControlAssessment]
    institutional_evidence: List[str] = field(default_factory=list)
    responsible_reviewer: Optional[str] = None


@dataclass
class GateResult:
    state: PathwayState
    reasons: List[str]
    next_action: str


REQUIRED_CONTROLS = (
    "justificatory",
    "participatory",
    "corrective",
    "anti_fettering",
)


def evaluate_egl_gate(pathway: EGLPathway) -> GateResult:
    """
    Evaluate whether an AI-assisted institutional pathway may advance.

    Technical completion alone never produces lawful closure.
    """

    reasons: List[str] = []

    missing_controls = [
        control
        for control in REQUIRED_CONTROLS
        if control not in pathway.controls
    ]

    if missing_controls:
        return GateResult(
            state=PathwayState.PAUSED,
            reasons=[
                "Missing required control assessments: "
                + ", ".join(missing_controls)
            ],
            next_action="Complete the four-control assessment.",
        )

    if not pathway.authority_confirmed:
        return GateResult(
            state=PathwayState.RESTRICTED,
            reasons=["Applicable institutional authority is not confirmed."],
            next_action="Identify and verify the lawful authority basis.",
        )

    if not pathway.responsibility_boundary_confirmed:
        return GateResult(
            state=PathwayState.RESTRICTED,
            reasons=["The responsibility boundary is unresolved."],
            next_action="Assign accountable institutional responsibility.",
        )

    if pathway.participation_required and not pathway.participation_completed:
        return GateResult(
            state=PathwayState.RETURNED,
            reasons=[
                "Required notice, disclosure, response, or correction "
                "opportunity has not been completed."
            ],
            next_action="Return the pathway to the participation stage.",
        )

    if pathway.material_dispute:
        return GateResult(
            state=PathwayState.ESCALATED,
            reasons=[
                "A material factual, classification, or routing dispute remains."
            ],
            next_action="Escalate to an authorized independent reviewer.",
        )

    if not pathway.correction_available:
        return GateResult(
            state=PathwayState.PAUSED,
            reasons=["A practical correction or review mechanism is unavailable."],
            next_action="Establish return, reopening, review, and remedy functions.",
        )

    if not pathway.human_override_available:
        return GateResult(
            state=PathwayState.RESTRICTED,
            reasons=[
                "The human reviewer lacks genuine authority to depart "
                "from the machine-shaped output."
            ],
            next_action="Restore effective human discretion.",
        )

    failed_controls = [
        name
        for name, assessment in pathway.controls.items()
        if assessment.status == ControlStatus.FAILED
    ]

    if failed_controls:
        return GateResult(
            state=PathwayState.RETURNED,
            reasons=[
                "Failed mandatory controls: " + ", ".join(failed_controls)
            ],
            next_action="Return the pathway for control remediation.",
        )

    partial_controls = [
        name
        for name, assessment in pathway.controls.items()
        if assessment.status == ControlStatus.PARTIAL
    ]

    if partial_controls:
        return GateResult(
            state=PathwayState.PAUSED,
            reasons=[
                "Partially satisfied controls: " + ", ".join(partial_controls)
            ],
            next_action="Complete and evidence the outstanding controls.",
        )

    unsupported_not_applicable = [
        name
        for name, assessment in pathway.controls.items()
        if (
            assessment.status == ControlStatus.NOT_APPLICABLE
            and not assessment.reason.strip()
        )
    ]

    if unsupported_not_applicable:
        return GateResult(
            state=PathwayState.PAUSED,
            reasons=[
                "NOT_APPLICABLE status lacks justification: "
                + ", ".join(unsupported_not_applicable)
            ],
            next_action="Record the legal and institutional justification.",
        )

    if not pathway.institutional_evidence:
        return GateResult(
            state=PathwayState.PAUSED,
            reasons=["No institutional evidence record has been supplied."],
            next_action="Attach a review-ready institutional evidence record.",
        )

    if not pathway.responsible_reviewer:
        return GateResult(
            state=PathwayState.PAUSED,
            reasons=["No responsible human reviewer has been identified."],
            next_action="Assign an authorized human reviewer.",
        )

    reasons.append("All mandatory EGL controls are satisfied and evidenced.")

    return GateResult(
        state=PathwayState.READY_FOR_TRANSMISSION,
        reasons=reasons,
        next_action=(
            "Transmit through GTL for authorized human or institutional "
            "closure. Do not treat technical completion as lawful closure."
        ),
    )


if __name__ == "__main__":
    satisfied = ControlAssessment(
        status=ControlStatus.SATISFIED,
        evidence_refs=["record-001"],
    )

    example = EGLPathway(
        pathway_id="EGL-DEMO-001",
        node_id="pre-closure-review",
        risk_tier="HIGH",
        authority_confirmed=True,
        responsibility_boundary_confirmed=True,
        participation_required=True,
        participation_completed=True,
        correction_available=True,
        human_override_available=True,
        material_dispute=False,
        controls={
            "justificatory": satisfied,
            "participatory": satisfied,
            "corrective": satisfied,
            "anti_fettering": satisfied,
        },
        institutional_evidence=["record-001"],
        responsible_reviewer="Authorized Institutional Reviewer",
    )

    result = evaluate_egl_gate(example)

    print("Pathway state:", result.state.value)
    print("Reasons:", result.reasons)
    print("Next action:", result.next_action)
