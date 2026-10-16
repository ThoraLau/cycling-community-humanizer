# Audience profile

## Core audience

Experienced adult cyclists in the United States, United Kingdom, and Canada, generally 30+, including serious enthusiasts, bicycle mechanics, coaches, amateur and professional racers, commuters, tourers, club riders, bike-fit customers, and cycling-kit enthusiasts.

The initial source list has an older male skew, but it also includes women cyclists and multiple cycling subcultures. Do not flatten these groups into one persona. Demographic details guide sampling; they are not writing cues by themselves.

Readers usually know the basics. They tend to value concrete setup details, observed trade-offs, repairability, fit, weather, road or trail conditions, cost, and actual use cases more than lifestyle claims.

## Source map

Primary community labels: r/cycling, r/bicycling, r/bicycle, r/bikewrench, r/Biking, r/Velo, r/bicycleculture, r/ladycyclists, r/CyclingFashion, r/bikefit, r/bikecommuting, r/bicycletouring, r/BicyclingCirclejerk, r/londoncycling, and r/RoadBikes.

Use subreddit names only as source labels. Do not automatically crawl Reddit; see `corpus-policy.md`. Keep r/BicyclingCirclejerk in a separate satire register.

Escape Collective is an editorial reference and must retain `source_type=editorial`; do not mix its polished prose blindly with forum comments.

Instagram, Strava, Meetup, and private cycling groups are context-only sources unless the user supplies an authorized export. Anonymize private messages and club chats during ingestion.

## Formats

- Long-form blogs and explainers
- Component, apparel, accessory, and bike reviews
- Forum posts and replies
- Social captions and spoken short-video scripts
- Club or customer email

## Locale handling

- `en-US`: tire, aluminum, center; US units where appropriate.
- `en-GB`: tyre, aluminium, centre; units according to source context.
- `en-CA`: Canadian spelling where natural; units depend on context.

Use one locale per output. If unspecified, retain the input spelling and units. If the input gives no signal, use neutral international English and do not convert measurements.
