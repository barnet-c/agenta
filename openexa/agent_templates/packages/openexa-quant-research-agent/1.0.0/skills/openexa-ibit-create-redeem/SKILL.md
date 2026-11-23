---
name: openexa-ibit-create-redeem
description: "Playbook for the IBIT ETF create and redeem arbitrage lifecycle. Use for any task about IBIT premium or discount to spot BTC, the 3:45 to 4:00 PM ET close window, or a create or redeem proposal."
---

Use this with the openexa-governed-swarm skill. This playbook is the single source for how the IBIT lifecycle is judged. If an agent prompt disagrees with it on the facts, this playbook wins. On rules and gates, the governance skill wins.

## The window

- The primary window is 3:45 PM to 4:00 PM US Eastern market time (ET) on trading days. Creation and redemption orders settle then, and basis is priced against end-of-day NAV.
- Always show ET and UTC. ET is EDT for most of the year, so never treat it as a fixed UTC-5.

## The edge test

- **Create signal:** IBIT trades rich to spot BTC (a premium). Path: buy spot BTC, deliver it to the trust, sell IBIT shares.
- **Redeem signal:** IBIT trades cheap to spot BTC (a discount). Path: buy IBIT shares, redeem with the trust, sell spot BTC.
- **Gross edge** is the premium or discount in basis points (bps) against the value per share implied by spot BTC. A positive number is a premium (the CREATE side). A negative number is a discount (the REDEEM side).
- **Net edge** is the size of the gross edge (ignore the sign) minus round-trip costs (fees, commission, market impact, slippage). Subtract costs once. Example: a 2.4 bps discount with 7.6 bps of costs gives net edge of -5.2 bps, not -10.0.
- **Margin over the hurdle** is net edge minus the hurdle. The hurdle is a bar to clear, not another cost. Never subtract it from net edge and still call the result net edge.
- **Go or no-go:** go only if net edge is positive and the margin over the hurdle is positive.
- **Worked example** (illustrative numbers): gross edge 22.93 bps, round-trip cost 12 bps, hurdle 5 bps. Net edge is 10.93 bps. Margin over the hurdle is 5.93 bps. Result: pass.
- Always report all four numbers (gross edge, costs, net edge, margin over the hurdle) so a reader can check the arithmetic.
- If you do not have the hurdle or a cost input, say so. Never substitute a guess.

## Desk parameters

These are the desk's own numbers, taken on 2026-10-05 from the signal logic of the desk's IBIT bot, which matches the dashboard. If the dashboard ever shows different numbers, report both and flag it.

- Creation unit: 40,000 shares.
- Bitcoin per share (desk constant): 0.000566243.
- Create or redeem fee: $700 per creation unit.
- ETF commission: $0.005 per share.
- Bitcoin execution cost: 0 bps.
- Market impact: 1 bp per leg, so 2 bps for the round trip.
- Bitcoin spot spread: 1 bp.
- Hurdle (minimum spread left after costs): 5 bps.

Formulas, with the IBIT price P in dollars:

- Round-trip cost in bps = 225 / P + 3. (The fee is $0.0175 per share, which is 175 / P bps. Commission is 50 / P bps. Impact is 2 and spot spread is 1.)
- Trigger in bps = cost + hurdle = 225 / P + 8.
- Implied value per share = Bitcoin per share x spot BTC.
- Gross edge in bps = (IBIT mid - implied value) / implied value x 10,000.
- Net edge in bps = |gross edge| - cost. Margin over the hurdle = net edge - hurdle.
- Signal: CREATE if gross edge is above the trigger. REDEEM if it is below minus the trigger. Otherwise NEUTRAL.
- Example at P = $48.66: cost 7.62 bps, trigger 12.62 bps.

The desk's bot also waits for a signal to hold for 2 polls in a row, leaves 60 seconds between entries, and acts only from 9:30 AM to 4:00 PM ET on weekdays. Mention these when comparing with the bot.

## Known data issues

- Official NAV per share is a daily 4:00 PM snapshot. After hours, or before the new NAV posts, comparing the live price with it is not like for like. On 2026-10-05 the feed still showed the 2026-10-02 NAV, which made the gap look like 215 bps. For the live gap use the implied value. Use the official NAV only near the close, with a same-day NAV.
- The market overview feed's `btc_per_share` is worked out from an older NAV and a moving reference price, so it jumps between days (0.0005625 on 2026-10-02, 0.0005661 on 2026-10-05). Use the desk constant as the main figure and the feed's value as a cross-check. If the two give implied values more than 5 bps apart, say so and mark the signal UNCONFIRMED until a human confirms the figure.
- The desk constant drifts slowly as the fund's fee accrues. A human should refresh it from the fund's published figure, and you should say "constant as of 2026-10-05".
- The dashboard's explainer text mentions 5,000-share baskets while its numbers use 40,000. Treat 40,000 as the desk setting, and flag the mismatch if basket size matters to the result.

## Data sources

- IBIT Create and Redeem dashboard: https://calm-sea-07333b91e.7.azurestaticapps.net/
- Coinbase BTC-USD spot ticker: https://api.exchange.coinbase.com/products/BTC-USD/ticker
- Market overview API: https://btctrader-api-68276-gqbkg8bucfbndjgn.z01.azurefd.net/api/market-overview
- Record the timestamp and source of every number. Anything older than the current window is stale.

## What to report

Mid price, spot BTC, NAV and implied value, signal (CREATE, REDEEM, NEUTRAL or UNCONFIRMED), gross edge, costs, net edge and margin over the hurdle in bps, basket size, estimated profit and loss, capital required, and risk factors such as basis risk and timing delay. Label estimates as estimates.

## Who does what

Analysts observe and recommend. Strategy predicts. The Portfolio Manager proposes. Risk and Compliance check. The Execution Council approves. The Trader prepares an execution plan. Nothing in this playbook executes a trade.
