angou\_binance 3 (May 24, 2018)
===
- `angou_binance.rest.RestSession` now takes an optional `timeout` argument,
  instead of `request_kwargs`.
- `Content-Type` HTTP header is now set to `application/x-www-form-urlencoded`,
  as Binance REST API requires.


angou\_binance 2 (May 24, 2018)
===
- `angou_binance.rest` now exposes a module-scoped `LOGGER` variable, instead of
  per-class `angou_binance.rest.RestSession.logger`s.
- If a response has a “success” HTTP status code but its body cannot be parsed
  as JSON, `angou_binance.rest.InvalidJSON` is raised.
- `angou_binance.rest.RestSession` constructor now takes an optional argument
  `request_kwargs` that is passed as `**kwargs` to `request.Request` object
  constructor.

angou\_binance 1 (May 19, 2018)
===
The first release of angou\_binance!
