# Volume 46 — Bilingual Record Structure Audit: 3610–3624

## Scope

This audit was triggered while preparing the corrective completion of Batch 6 (3620–3624). The master processing guide and locked Volume 46 translation conventions require each bilingual record to contain the complete available `Original Tamil — மூலத் தமிழ்`, not merely links to canonical page files.

Scope checked: **letters 3610–3624**.

## Governing requirements

- `VOLUME_PROCESSING_GUIDE.md` §10 requires bilingual order ending with the complete available `Original Tamil — மூலத் தமிழ்`.
- `VOLUME_PROCESSING_GUIDE.md` §11 requires the appended Tamil to match the canonical pages before source-check/alignment completion.
- `PILOT_TRANSLATION_CONVENTIONS.md` convention 12 states that the complete audited Tamil is reproduced with the bilingual record.

## Finding

The structural omission is **not limited to Batch 6**.

The repository file inventory and direct file inspection show that the regression begins at **3610** and continues through **3624**. These records contain an `Original Tamil — மூலத் தமிழ்` heading followed only by links/a statement pointing to canonical page files; they do not reproduce the complete audited Tamil inside the bilingual record.

Affected range:

- Batch 4: **3610–3614** — currently marked verified, but structurally incomplete.
- Batch 5: **3615–3619** — currently marked verified, but structurally incomplete.
- Batch 6: **3620–3624** — draft/alignment-reviewed and already withheld from verification for this defect.

The earlier pilot and Batches 1–3 (3592–3609) have substantially larger bilingual records consistent with the established complete-bilingual-record pattern; they are not included in this corrective scope unless a later direct content audit proves otherwise.

## Status consequence

The meaning-level bilingual reviews already completed for 3610–3619 are not discarded. Their English alignment findings remain valid. However, the files do **not** presently satisfy the repository's final bilingual-record structure, so their `verified` status must not be treated as release-complete until the complete canonical Tamil appendices are restored and checked.

For 3620–3624, the existing Batch 6 alignment result remains valid: 3620, 3621, 3622 and 3624 pass meaning-level review; 3623 requires the two documented English corrections. None of 3620–3624 should be promoted until structural completion.

## Corrective plan

1. Repair **3610–3614** as one corrective batch: append the complete fidelity-cleared canonical Tamil to each bilingual file and recheck appendix equality against the canonical page sequence.
2. Repair **3615–3619** the same way.
3. Repair **3620–3624**: restore translator-note blocks where absent, append complete canonical Tamil, apply the two documented 3623 English corrections, and recheck all five.
4. Only after each corrective batch passes, synchronize statuses/progress/README metadata.
5. Do not begin 3625–3629 drafting until the structural regression through 3624 is closed.

## Source protection

This audit makes **no canonical Tamil changes**. Canonical `pages/page-NNN.md` files remain authoritative. The corrective work must copy their audited text without modernization, normalization, reconstruction or outside-source substitution.
