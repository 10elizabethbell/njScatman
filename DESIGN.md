---
name: NJ Scatman
description: A live South Jersey backyard lawn that sells a clean yard and a free first week on one phone screen.
colors:
  night: "#16351f"
  night-2: "#1c4226"
  lawn: "#3f7f34"
  lawn-light: "#8cc152"
  cream: "#f7f2e3"
  cream-2: "#efe6cf"
  paper: "#fffaf0"
  straw: "#cdbf9b"
  ink: "#33210f"
  ink-soft: "#5e4527"
  brown: "#6b3f1d"
  mustard: "#f5c533"
  mustard-hover: "#ffd34d"
  on-night: "#f7f2e3"
  on-night-soft: "#c9d9b8"
  error-line: "#b3261e"
  error-text: "#9c1f17"
typography:
  display:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(40px, 12.4vw, 92px)"
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(34px, 9vw, 64px)"
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: "-0.02em"
  price:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(46px, 14vw, 64px)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.03em"
    fontFeature: "tnum"
  title:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "20px"
    fontWeight: 800
    lineHeight: 1.2
  pitch:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(16px, 4.6vw, 20px)"
    fontWeight: 400
    lineHeight: 1.45
  body:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 900
    letterSpacing: "0.04em"
  small:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.45
rounded:
  pill: "999px"
  ticket: "24px"
  frame: "22px"
  field: "14px"
  mark: "12px"
spacing:
  gutter-phone: "16px"
  gutter-desk: "32px"
  section-phone: "56px"
  section-desk: "96px"
  stack: "28px"
  chip-gap: "8px"
  pair-gap: "10px"
components:
  button-gold:
    backgroundColor: "{colors.mustard}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0 22px"
    height: "56px"
  button-gold-hover:
    backgroundColor: "{colors.mustard-hover}"
  button-ghost-on-night:
    backgroundColor: "transparent"
    textColor: "{colors.on-night}"
    rounded: "{rounded.pill}"
    padding: "0 22px"
    height: "56px"
  button-ghost-on-cream:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0 22px"
    height: "56px"
  chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0 18px"
    height: "48px"
  chip-selected:
    backgroundColor: "{colors.night}"
    textColor: "{colors.cream}"
  field:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "0 16px"
    height: "54px"
  ticket:
    backgroundColor: "{colors.night}"
    textColor: "{colors.cream}"
    rounded: "{rounded.ticket}"
    padding: "22px 18px 18px"
  service-row-mark:
    backgroundColor: "{colors.night-2}"
    textColor: "{colors.lawn-light}"
    rounded: "{rounded.mark}"
    size: "40px"
  fact-chip:
    backgroundColor: "{colors.cream-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "6px 14px"
  photo-frame:
    backgroundColor: "{colors.night-2}"
    rounded: "{rounded.frame}"
  sticky-bar:
    backgroundColor: "{colors.night}"
    padding: "10px 12px"
---

# Design System: NJ Scatman

## Overview

**Creative North Star: "The Living Backyard"**

The whole page is one South Jersey lawn. The ground is deep lawn green, never black; cream sections are the paths and patios cut into it. Every green edge is live grass, and every blade, fringe and path edge reads the same wind, so the page moves as one yard rather than as a stack of animated widgets. The client's own materials set the palette: greens from the logo oval, chocolate brown from the wordmark, mustard from the "First Week is FREE" starburst. Their Doberman-detective mascot stands in the hero grass with its feet sunk into the blades.

Density is phone-first and generous: one column, big tap targets (44px minimum, 48 to 56px for anything primary), heavy uppercase display headings over plain sentence-case body. The voice is cartoon and cheeky, never gross: piles are drawn like the one in the logo, with flies and a scoop gesture, never photographic.

Interaction is tactile. Grass parts and springs back under a finger or mouse; piles are scooped with a swipe; service rows toggle add-ons into the plan picker. Motion pauses off screen and freezes to a single still frame under reduced motion.

**Key Characteristics:**
- Deep lawn-green ground with cream "path" sections; no black anywhere.
- One shared wind drives every grass canvas and every wavy cream edge.
- System font stack: 900-weight uppercase display, 17px sentence-case body.
- Pill buttons in matched pairs: same height, same 2px outline, gold plus ghost.
- Photos sit inside the world's material: rounded frames with live grass lapping their base.
- Phone-first, with a sticky two-button contact bar under 900px.

## Colors

A three-family palette lifted from the client's logo and starburst: lawn greens for ground, cream and paper for surfaces, brown and mustard for voice and action.

### Primary
- **Starburst Mustard** (mustard): the one action color. Gold buttons, the hero headline's emphasized phrase, the ticket's "First week FREE" note, the "Added to your plan" confirmation, row arrow hover, focus rings, text selection, and the scoop hint's done state. Its hover is a lighter **Sunlit Mustard** (mustard-hover).

### Secondary
- **Wordmark Brown** (brown): form legends and labels, the close section's county line, the field caret, chip hover border. Brown speaks for the brand on cream; it is never a button fill.

### Tertiary
- **Logo Oval Green** (lawn-light): the brightest grass blade color and the service-row icon color on night.
- **Lawn** (lawn): the static grass-gradient fallback under the hero before JS paints the canvas; mid-tone of the grass family.

### Neutral
- **Deep Lawn Night** (night): page ground, hero, services, footer, the price ticket, selected chips, the sticky bar (at 94% opacity), translucent hint and caption pills (at 78 to 82%).
- **Night Moss** (night-2): one step up from night, for service-row icon tiles and photo frame backing.
- **Path Cream** (cream): cream section ground and primary text on night (on-night is the same value, named for its role).
- **Sun-Faded Cream** (cream-2): fact chips in the close section.
- **Paper** (paper): chip and input fill; a hair brighter than cream so controls lift off the path.
- **Straw** (straw): chip and input resting border.
- **Bark Ink** (ink): text on cream and on mustard; the gold button's outline.
- **Soft Bark** (ink-soft): secondary copy on cream.
- **Sage** (on-night-soft): secondary copy on night, price units, footer text; at 22% alpha it is the hairline between service rows.
- **Error** (error-line, error-text): the town field's border and message when a send is attempted without a town.

### Grass palette (canvas only)
The grass is painted from a fixed ladder of greens, back to front, dark to light: #1f4a26, #255a2b, #2a6230, #2f6e30, #3a7f35, #347533, #4d9a3d, #6cb44a, #8cc152, #5ea844. Fringes end their front layer in night and night-2 so the blades melt into the green section they grow from. These are recorded with each layer in `.impeccable/design.json`.

### Named Rules
**The Never-Black Rule.** The darkest surface is Deep Lawn Night. Shadows and overlays are tinted with it (rgba(22,53,31,…)), not with neutral black, except the soft drop under gold buttons and photo frames.

**The One Gold Rule.** Mustard is reserved for action, confirmation and focus. If it is not clickable, focused, or confirming something the visitor did (or the free-week offer itself), it is not mustard.

## Typography

**Display Font:** system-ui (with -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif)
**Body Font:** the same stack
**Label Font:** the same stack, at weight 900 uppercase

**Character:** One family at two extremes: shouting 900-weight uppercase with tight tracking for headlines and prices, plain relaxed sentence case for everything a visitor actually reads. The client's rounded wordmark face lives only in their logo image. This is Ellie's confirmed house style (fast, no font load), not a default left in place.

### Hierarchy
- **Display** (900, clamp(40px, 12.4vw, 92px), 0.95, uppercase, max 11ch, balanced wrap): the hero headline only. One phrase may be colored mustard for emphasis.
- **Headline** (900, clamp(34px, 9vw, 64px), 0.95, uppercase, balanced): section titles. The close section's headline runs larger (clamp(40px, 11vw, 76px)) as the page's second hero.
- **Price** (900, clamp(46px, 14vw, 64px), 1, -0.03em, tabular numerals): the live price on the ticket.
- **Title** (800, 20px, 1.2): service row titles.
- **Pitch** (400, clamp(16px, 4.6vw, 20px), 1.45, max 34ch): the one-line pitch under the hero headline; key facts in bold cream inside sage text. 20px is the ceiling.
- **Body** (400, 17px, 1.5): all running copy; intros cap at 44ch.
- **Label** (900, 15px, 0.04em, uppercase, brown): form legends and field labels only.
- **Small** (15px): notes, errors, footer, fact chips, ticket sub-lines. Nothing readable goes below 13px (13px is reserved for photo captions and the ticket's "Your message" label).

### Named Rules
**The Two Voices Rule.** Uppercase 900 is for headlines, prices and form labels. Everything else is sentence case. Never set a paragraph, a button, or a chip in uppercase.

## Layout

Phone-first single column inside a 1180px max wrap with 16px gutters (32px from 900px up).

- **Breakpoints:** 560px (paired controls go side by side: hero buttons, town/name fields, ticket send buttons; top-bar phone number appears; hero lawn 240px to 270px) and 900px (two-column grids, desktop hero, sticky bar removed).
- **Sections** pad 56px top / 64px bottom on phones, 96px / 104px on desktop.
- **Hero on phone:** top bar (64px) with badge and call pill, headline, pitch, stacked button pair, then a 240px lawn stage carrying the mascot and piles. Offer and both primary actions sit in the first 390px-wide viewport.
- **Hero on desktop:** at least min(860px, 100vh); copy on the left with 190px of bottom padding so the 520px absolutely positioned lawn grows up behind it; the mascot fills the right column and is never placed under the hero buttons.
- **Plan section:** picker 1.15fr / sticky ticket .85fr at 48px gap; the ticket sticks 24px from the top.
- **Services:** rows 1.1fr / photos .9fr at 56px gap. Photos are a two-column grid: one tall 4:3 frame spanning both columns over two 1:1 frames, 12px gaps.
- **Close:** logo .8fr / copy 1.2fr at 56px gap; on phone the logo is centered at min(260px, 70%).
- **Footer** carries 120px bottom padding on phones so the sticky bar never covers it.
- **Section order as shipped:** hero, plan picker, What I DOO (services + photos), close (logo, counties, contact), footer. The planned "How it works" section was cut in review because it only repeated the hero, the picker and the close; its empty CSS header remains in the stylesheet.
- **Rhythm:** 8px chip gaps, 10px between paired buttons, 14px between fields, 22px between fieldsets, 28px from a section intro to its content.

### Named Rules
**The First-Screen Rule.** On a 390px phone the offer, the free week, and both primary actions (claim + call) are visible without scrolling.

**The No-Hole Rule.** A desktop column that would sit empty gets proof in it (photos, the ticket, the logo), never decoration.

## Elevation & Depth

Depth is mostly material, not shadow: three overlapping layers of grass blades, cream paths over green ground, the mascot redrawn over the front blades so its starburst stays readable. Shadows are few, soft, and tinted. No hairline highlights, no inset glints, no hard offsets.

### Shadow Vocabulary
- **Ticket lift** (`box-shadow: 0 10px 30px -12px rgba(22,53,31,.45)`): the price ticket, the only lifted card on cream.
- **Gold button drop** (`box-shadow: 0 8px 20px -10px rgba(0,0,0,.55)`): under gold buttons so the primary action sits up off the ground.
- **Photo frame drop** (`box-shadow: 0 14px 30px -14px rgba(0,0,0,.6)`): photo frames on night.
- **Field focus halo** (`box-shadow: 0 0 0 3px rgba(245,197,51,.6)`): focused input, with border shifting to night.

### Named Rules
**The Solid Material Rule.** Anything that represents a material (grass, piles, flies) is drawn filled and shaded with body: piles use a three-stop radial gradient and a soft ground shadow. No outline-only shapes standing in for matter.

## Shapes

Everything a visitor touches is a full pill (999px): buttons, chips, the call link, the scoop hint, captions, fact chips. Containers are generously rounded but clearly not pills: ticket 24px, photo frames 22px, fields and the message preview 14px, service icon tiles 12px, add-on tick boxes 6px. Circles are used for the brand badge (46px) and the row arrow cue (40px). Borders are a uniform 2px on every control. The only organic edges are the grass silhouettes and the wavy cream path tops, both driven by wind.

## Components

### Buttons
Always used in matched pairs: one gold, one ghost, identical height and outline.
- **Shape:** full pill (999px), 2px border, min-height 56px (54px in the sticky bar), 22px horizontal padding, 10px icon gap, 800 weight 17px, no wrap.
- **Gold (primary):** mustard fill, ink text, ink outline, soft drop; hover lightens to Sunlit Mustard.
- **Ghost (secondary):** transparent with a 2px outline in the surrounding text color: cream on night and on the ticket, ink on cream. Hover adds a 10% cream wash on night or 6% ink wash on cream.
- **Press:** scale(.97) with a .25s cubic-bezier(.16,1,.3,1) spring.
- **Focus:** 3px mustard outline, 3px offset.
- **Pairing:** stacked on phones with 10px gap, side by side from 560px. The gold button carries an arrow icon trailing, the ghost a phone/mail icon leading.

### Chips (plan picker)
- **Style:** paper fill, 2px straw border, pill, min-height 48px, 18px padding, 800 weight. Dog-count chips are square-ish (min-width 56px, centered).
- **Hover:** border turns brown.
- **Selected:** night fill, night border, cream text, lifted 1px. Checkbox chips (add-ons) carry a 18px rounded tick box that fills with a check when on.
- **Focus:** 3px mustard outline at 2px offset on the visible chip.
- **Fact chips** (close section): non-interactive cream-2 pills at 15px/700, 6px 14px padding.

### Inputs / Fields
- **Style:** paper fill, 2px straw border, 14px radius, min-height 54px, 600 weight 17px, brown caret; uppercase brown label above.
- **Focus:** border to night plus the mustard focus halo.
- **Error:** border to error-line; error-text message at 15px/700 below. Triggered only when a send is attempted without a town; the field scrolls to center and focuses.

### Price Ticket (signature)
A night card on cream: 24px radius, ticket lift shadow, 22px 18px 18px padding (28px 26px 24px and sticky on desktop). Holds the live price (tabular), unit in sage, mustard offer note, sage sub-line, a "Your message" label over a 14px-radius preview well (8% cream wash, pre-wrap, max 180px scroll), then the gold/ghost send pair and an "or call" link. It is `aria-live` so price changes are announced.

### Service Rows
A divider list, not cards: rows separated by 1px sage hairlines at 22% alpha, 18px vertical padding. Each row: a 40px night-2 icon tile (12px radius, lawn-light stroke icon), title plus sage description, and on actionable rows a 40px circular arrow cue (2px cream at 45%) that fills mustard and nudges 3px right on hover/focus. The whole row is the button; there is one arrow per row and no repeated "Add" text. Add-on rows show a mustard "Added to your plan" line when their chip is checked, and toggle that chip.

### Photo Frames (signature)
Client photos inside 22px-radius frames on a night-2 backing with the photo drop shadow. A 52px grass canvas laps the bottom edge of every frame. Optional caption: a translucent night pill at top-left, 13px/800. Images are not draggable or selectable.

### Navigation
- **Top bar:** 64px (84px desktop). Left: 46px cream circle badge (a crop of the mascot's head) plus "NJ Scatman" at 900/19px. Right: a 44px pill call link with a 50%-cream outline; the number appears from 560px.
- **Sticky phone bar (under 900px):** fixed bottom, night at 94%, 1.35fr/1fr gold + ghost pair, safe-area aware. Slides up (.35s cubic-bezier(.2,.9,.3,1)) once the hero buttons scroll away; inside the plan section the gold label becomes "Send my request" and jumps to the ticket; it hides while the ticket's own send buttons are visible.

### Living Lawn (signature motion system)
One requestAnimationFrame loop (`YARD`, top of the script in `index.html`) drives every canvas and path edge. Items register with an IntersectionObserver (80px margin) and only visible items draw; the loop stops when nothing is on screen. Under `prefers-reduced-motion` each item paints one still frame. Exact constants are mirrored in `.impeccable/design.json` under `extensions.motion`.

- **Shared wind** (`YARD.wind(x, t)`): three sines at different speeds and directions (weights .55/.30/.15) under a slow wandering gust envelope (0.6 ± 0.4), sampled at page-x so neighboring canvases agree. Tempo knob: `WIND_SPEED` (1.0).
- **Pointer:** one shared pointer with smoothed velocity (decays ×0.9 per frame); scroll zeroes mouse velocity; touch canvases use `touch-action: pan-y` so swiping sideways scoops and vertical still scrolls.
- **Lawn class** (`function Lawn`): blades are quadratic-curve fills batched per layer color. Knobs: `SPACING` (4.2px phone / 3.2px desktop), `HEIGHT` ([40, 78] default), `LAYERS` (three back-to-front layers with lift 18 / 8 / -2 and their green ladders), `PUSH_R` (70px), spring `STIFF` 38 / `DAMP` 6.5, deflection clamped to ±1.25 rad. Lean = 0.08 rest tilt + wind × 0.32 × per-blade flex + spring offset. Device pixel ratio capped at 2. All lawns rebuild together on width change (150ms debounce).
- **Hero lawn:** blade height [40, 80] phone / [60, 120] desktop, reach 70 / 90. The mascot is drawn before the front layer so its feet sink in, then its starburst slice (x 53 to 90%, top 86%) is redrawn after the front layer so "is FREE" stays readable. Piles: `PILES_PHONE` 4 / `PILES_DESK` 7, spaced 1.6 sprite widths, kept off the starburst, the mascot's feet and the hint; sprite 36px phone / 38px desktop; each pops in with a staggered 140ms bounce and a six-blade tuft at its base. `SCOOP_R` 34px: a swipe within reach flings the pile up with gravity and spin (fades over .8s), scatters its two flies, and bursts nine clippings in grass greens and mustard. Flies orbit, flee the pointer within 70px, and flap fast. The hint pill counts "N left", turns mustard with "Spotless. That's the job.", and piles respawn after `RESPAWN_MS` 4200.
- **Fringes:** at the top of every green section that follows cream, a 58px canvas rises 46px into the cream: height [26, 52], reach 60, three layers ending in night/night-2 so blades grow out of the section.
- **Photo frame grass:** 52px canvases, height [18, 40], spacing 4.5 / 3.6, reach 50, two layers.
- **Path edges:** every cream section that follows green has a 28px SVG top edge whose path is rebuilt each frame from the same wind (`AMP` 5 viewBox units plus a 3-unit slow roll, sampled every 24 units).

### Named Rules
**The One Yard Rule.** Every moving edge reads `YARD.wind` at its page-x and runs in the one shared loop. A new animated surface joins the loop through `YARD.add`; it never starts its own timer.

**The Green-Edge-Is-Grass Rule.** Wherever green meets cream, the green side grows a live fringe and the cream side rolls with the wind. No straight hard edges between the two grounds.

## Do's and Don'ts

### Do:
- **Do** keep the ground Deep Lawn Night and tint overlays and the ticket shadow with it.
- **Do** ship buttons as matched gold/ghost pairs: 56px pills, 2px outline, same component everywhere.
- **Do** frame any client photo in a 22px-radius frame with grass lapping its base.
- **Do** run every new motion through the shared `YARD` loop and wind, pause it off screen, and paint a still frame under reduced motion.
- **Do** keep tap targets at 44px minimum and primary controls at 48 to 56px.
- **Do** make a whole row the button, with one arrow-in-a-circle cue, instead of repeating an action label.
- **Do** keep the pitch line at 20px max and let headlines wrap balanced.

### Don't:
- **Don't** use black or neutral grey surfaces; the darkest color is night.
- **Don't** use mustard for decoration; it marks action, confirmation, focus, or the free-week offer.
- **Don't** add thin decorative highlight lines, inset glints, or hard offset shadows.
- **Don't** draw materials as outlines; grass, piles and flies are filled and shaded.
- **Don't** make the piles or anything else graphic; cartoon, in the logo's own style.
- **Don't** set body copy, buttons or chips in uppercase.
