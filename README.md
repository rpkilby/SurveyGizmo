
# SurveyGizmo

A Python Wrapper for [SurveyGizmo](http://developer.surveygizmo.com/rest-api-documentation/)'s restful API service.

[![Build Status](https://travis-ci.org/ITNG/SurveyGizmo.svg?branch=master)](https://travis-ci.org/ITNG/SurveyGizmo)
[![codecov](https://codecov.io/gh/ITNG/SurveyGizmo/branch/master/graph/badge.svg)](https://codecov.io/gh/ITNG/SurveyGizmo)


## Installation

    $ pip install SurveyGizmo


## Usage

Start by instantiating the SurveyGizmo object and providing some configuration parameters. Options can also be set through the `config` property.

```python
from surveygizmo import SurveyGizmo

client = SurveyGizmo(api_version='v4')
client.config.api_token = "E4F796932C2743FEBF150B421BE15EB9"
client.config.api_token_secret = "A9fGMkJ5pJF1k"
```

Calls to the api are by object type then by function. For example,

```python
client.api.survey.list()
client.api.survey.get('39501')
client.api.survey.copy('39501', '39501 Copy')
client.api.surveyresponse.list('39501')
```


## Authentication

Token based authentication is the only currently supported authentication method. `user:pass` and `user:md5` were [deprecated](https://community.surveygizmo.com/questions/question/final-notice-surveygizmo-api-authentication-changes/) on May 31, 2016. Oauth support is not currently a goal, but pull requests are welcome.

#### token
```python
client.config.api_token = 'E4F796932C2743FEBF150B421BE15EB9'
client.config.api_token_secret = 'A9fGMkJ5pJF1k'
```


## Config paramaters

* **api_version** - 'v3', 'v4', 'head'. Defaults to 'head'
* **api_token**
* **api_token_secret**
* **response_type** - `None`, `'json'`, `'pson'`, `'xml'`, `'debug'`. By default (using `None`), the API returns a JSON response which is parsed by the client into a python dictionary. Specifying a `response_type` will return an unparsed body of the specified format.
* **requests_kwargs** - Additional arguments passed to `requests.get`. Useful for setting timeouts and otherwise configuring the requests library.
* **prepare_url** - Force the client to return the url after being prepared instead of executing the api call. This is useful in cases where you need to call the api asynchronously. Defaults to 'False'
* **handler52x** - Handler for CloudFlare's 52x errors. Expects a callable (e.g., `surveygizmo.default_52xhandler`). Defaults to 'None'.


## Filters

A `filter` method has been added as a convenience for `list()` calls.

```python
client.api.filter('datesubmitted', '<=', '2013-07-01')
client.api.surveyresponse.list('39501')
```


Filters are chainable.

```python
client.api.filter('datesubmitted', '>=', '2012-07-01').filter('datesubmitted', '<', '2013-07-01').list('39501')
```


## CloudFlare 52x Errors

After SurveyGizmo's move to CloudFlare, it isn't uncommon to see connectivity issues where the service is temporarily unreachable. These errors exist on the 52x range of HTTP status codes. To automatically handle 52x errors, set a callable for `config.handler52x`. A basic handler is provided under `surveygizmo.default_52xhandler`, which simply retries the request every second until a non-52x response is returned.


## 1.0.0 Changelog

- Replace all authentication methods with only token based authentication.
- Rewrite API to use class inheritance instead of module function wrapping.
- Remove `preserve_filters` option.
- Rename `add_filter` to just `filter`. Filters are chainable.


## 0.2.0 Changelog

0.2.0 is a forwards incompatible release, but only minorly so.

Forwards incompatible changes:

- Renamed the 'change' operations to 'update'. This is consistent with SurveyGizmo's API naming.
- Removed the 'keep' kwarg for preserving filters bettween api funcion calls. This is now configured with 'preserve_filters'. Filters are now cleared manually with `api.clear_filters()`
- Removed the undocumented 'url_fetch' kwarg, which prevented api executioned and instead returned the prepared url.

Backwards incompatible changes:

- Modified 'api_version' to no longer has any effect on the client. SurveyGizmo provides no way to meaningfully differentiate between API versions, so this checking was unneeded and created code duplication
- Added 'prepare_url' as a replacement for 'url_fetch'. This forces the client to return the url after being prepared instead of executing the api call. This is useful in cases where you need to call the api asynchronously.
- Added 'requests_kwargs'. These are additional arguments passed to `requests.get`. Useful for setting timeouts and otherwise configuring the requests library.
- Added handling for CloudFlare 52x errors


## Copyright & License
Copyright &copy; 2013-2014 NC State University. See LICENSE for details.

