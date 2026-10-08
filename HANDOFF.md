# NJ Scatman — handoff at ~60%

**Live file:** index.html · **Repo:** https://github.com/10elizabethbell/njScatman · **Built:** 2026-10-08 from Muse brief 2026-10-08 (Marlton NJ Local Business Group post)

## What's built
- A focused "First week FREE — pick your plan" landing page (the brief's suggested shape), linkable from Facebook or from their existing nj-scatman.com. Not a full replacement site.
- **World: their backyard lawn.** Deep lawn-green ground, cream sections, mustard from their starburst, brown from their wordmark. Their own Doberman-detective mascot + "First Week is FREE" starburst (from nj-scatman.com) stands in the hero grass.
- **Signature element:** canvas grass that sways in layered wind and parts/springs back under mouse or finger. Cartoon piles (styled like the one in their logo) sit in the grass with flies circling; swipe over one and it's scooped (flies off, grass clippings burst). Counter "Swipe to scoop · N left" → "Spotless. That's the job." → piles return after ~4s. Same grass grows along every green section edge and laps the bottom of each photo; cream sections have a wind-driven wavy top edge. One shared animation loop, paused off screen, still frame under reduced motion, fewer blades on phones.
- **Plan picker:** how often (weekly / bi-weekly / twice a week / one-time), dogs (1–5+), add-ons, town, name → shows their published price and writes the request; sends by `sms:` or `mailto:`, with a call link. Town is required (inline error). Service rows for add-ons toggle them into the picker.
- Sections: hero → pick your plan → What I DOO (services + 3 Zeus photos in grass frames) → "First week's on us" (logo, counties, cancel-anytime line, contact) → footer with "Demo one-pager — free sample." A "How it works" section was cut in review: it only repeated the hero, picker and close.
- Phone: sticky bottom bar (Claim free week + Call) appears after the hero buttons scroll away; inside the picker it becomes "Send my request" (jumps to the price ticket) and hides over the ticket's own send buttons. ~250 KB single file; images load from embedded data after the motion starts.
- Top-bar badge is a crop of the Doberman's head from their logo (the full logo is unreadable at 46px); the full logo sits in the close section.
- Their mascot art is redrawn over the grass in the starburst area, so "is FREE" stays readable while the dog's feet sink into the lawn.
- `tools/embed-images.py` re-embeds `assets/*.webp` into index.html after a photo swap.

## Assumptions I made
- **Prices are shown.** The brief says no price list was published, but nj-scatman.com (fetched 2026-10-08) lists: weekly 1–4 dogs $19 / $21.50 / $24 / $26.50 per cleanup; bi-weekly 1–2 dogs $32.50 / $37; one-time $40 per 30 minutes; "Prices do not include tax". Used exactly. Their twice-a-week list is garbled ("3 Dogs – $19", "4 Dogs – $2o"), so twice-a-week shows "Ask". Also note bi-weekly costs more per cleanup than weekly — plausible, but confirm.
- One image alt on their site says "from $16.50 per week" — conflicts with the $19 list, not used.
- Service area = Burlington, Camden, Gloucester (brief). Their site's map also shades **Atlantic** county — left out until confirmed.
- First week free applies to recurring plans only; one-time scoop shows "No plan needed" instead. Inferred.
- Primary action = "Claim my free week" (goes to the picker) + Call. Texting is offered but **texts are unconfirmed**, so email and call sit right beside it.
- Headline uses their caption verbatim ("I DOO the dirty work"). Service copy is from their caption, flyer and site, lightly trimmed.
- Colors inferred from the logo (oval green, wordmark brown) and starburst (mustard). Ground is deep lawn green, not black.
- Zeus (the terrier in their site photos) is presumably the owner's dog; captioned neutrally. Photos with a person in them were skipped.
- Kept system fonts (house style). Their wordmark is a rounded display face; the logo image carries it.

## Placeholders and gaps
- No owner name, hours, reviews, before/after photos, Google Business Profile.
- No work photos (yards before/after) — only Zeus photos and their cartoon art.
- Twice-a-week prices, and 3+ dogs bi-weekly, show "Ask".

## Questions for the owner
- Do you take texts at 609-582-3709? (If not, swap "Text my request" for call-first.)
- Twice-a-week price list? Bi-weekly for 3–4 dogs?
- Do you serve Atlantic county?
- Does the free first week apply to every plan? Any contract/minimum?
- Add-on prices (deodorize/sanitize, fly bags, haul-away)?
- Can we use your name/face, and any before/after yard photos?
- What day(s) do you service each town? Gate/locked-yard policy?
- Is the shelter-dog spotlight something you want kept (on its own page, maybe)?

## Ideas not built (yours to pick)
- **Runner-up world: noir detective** (the mascot is a fedora'd private eye): a flashlight beam that follows the finger across a night yard, finding piles — "case closed". Stronger story, less "lawn".
- Mascot as a cut-out that reacts (tips hat) when the yard's spotless; or hands the scooped piles into a bag like the logo.
- Address autocomplete / county check ("You're in Burlington county — we cover you").
- A shelter-dog spotlight page, if the owner confirms it matters to them (brief says leave it out for now).
- Real booking (Calendly/Square) if they want online scheduling and payments.
- Self-host their rounded wordmark-style face for headings (would break house system-font rule; ask).

## Known leftovers
- The mascot art has a pale grey ground shadow that shows a little through the grass on desktop; painting it out of `assets/mascot.webp` would fix it.
- Detector flags the price ticket's offset shadow as a "dark glow"; it's a false positive (10px offset, on cream), left as is.
- Tuning knobs: `WIND_SPEED` (YARD), `SPACING`/`HEIGHT`/`PUSH_R` (Lawn), `PILES_PHONE`/`PILES_DESK`/`SCOOP_R`/`RESPAWN_MS` (hero), `AMP` (path edges), `PRICES` (picker).

## Not verified
- Real-device touch, and real SMS handoff on iOS/Android (`sms:+16095823709?&body=`), inside Facebook's in-app browser.
- Frame rate on older phones (phone ~280 blades + piles + 3 photo fringes).
- Contrast was checked by eye, not computed (detector ran in degraded regex mode).
