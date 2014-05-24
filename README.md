Read-only proxy for [TempoDB](http://tempo-db.com).

## Configuration

The TempoDB API key, secret and database ID must be set via
environment variables:

 - `TEMPODB_API_KEY`
 - `TEMPODB_API_SECRET`
 - `TEMPODB_DATABASE_ID`

## Usage

The proxy forwards all requests to `/tempodb/...` to TempoDB, using
the configured API key. Only GET requests are forwarded, making access
read-only.

## Deploying

The proxy is written in Python using Flask and can easily be deployed,
for example, at
[Heroku](https://devcenter.heroku.com/articles/getting-started-with-python).
