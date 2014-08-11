
# SurveyGizmo

A Python Wrapper for [SurveyGizmo](http://developer.surveygizmo.com/rest-api-documentation/)'s restful API service. Sort of - it's not really finished at the moment.


## Installation

    $ pip install SurveyGizmo

## Usage

Start by instantiating the SurveyGizmo object and providing some configuration parameters. Options can also be set through the `config` property.

```python
from surveygizmo import SurveyGizmo

sg = SurveyGizmo(api_version='v3', response_type='json')
sg.config.auth_method = "user:pass"
sg.config.username = "username"
sg.config.password = "password"
```

Calls to the api are by object type then by function. For example,

```python
sg.api.survey.list()
sg.api.survey.get('39501')
sg.api.survey.copy('39501', '39501 Copy')
sg.api.surveyresponse.list('39501')
```

## Authentication

Currently, `user:pass` and `user:md5` are the only supported authentication methods. There is the `oauth_helper` module that is built on top of [rauth](https://github.com/litl/rauth), but it remains untested. You can try it I guess.

#### user:pass
```python
sg.config.auth_method = 'user:pass'
sg.config.username = 'username'
sg.config.password = 'password'
```

#### user:md5
```python
sg.config.auth_method = 'user:md5'
sg.config.username = 'username'
sg.config.md5_hash = '5f4dcc3b5aa765d61d8327deb882cf99'
```
or you can provide a password to `config.password` and it will be automatically hashed.

#### oauth
```python
sg.config.auth_method = 'oauth'
sg.config.consumer_key = 'f5e5f0fc0300519c7gef3f4cddec396cf3d28cf192f'
sg.config.consumer_secret = 'dfa3fb80a5be5a08c5b427dbs9c4vb1ad3'
sg.config.access_token = '12345'
sg.config.access_token_secret = '54321'
```

## Config paramaters

* **api_version** - 'v3', 'v4', 'head'. Defaults to 'head'
* **auth_method** - 'user:pass', 'user:md5', 'oauth'
* **username**
* **password**
* **md5_hash**
* **consumer_key**
* **consumer_secret**
* **access_token**
* **access_token_secret**
* **response_type** - None, 'json', 'pson', 'xml', 'debug'. If None, the response is returned as a python dictionary.
* **requests_kwargs** - Additional arguments passed to `requests.get`. Useful for setting timeouts and otherwise configuring the requests library.
* **prepare_url** - Force the client to return the url after being prepared instead of executing the api call. This is useful in cases where you need to call the api asynchronously. Defaults to 'False'
* **preserve_filters** - Preserve filters between api calls. Defaults to 'False'. When 'True', use 'api.clear_filters' to manually clear the filters.

## Filters

Filters are currently untested (as is the whole library), but they should work. There is no magic here, just a convenience wrapper around the annoying filtering semantics. You could manually construct and pass these 

    TODO: Test filters

To filter, add filters to the query before making the api call. eg,

```python
sg.api.add_filter('datesubmitted', '<=', '2013-07-01')
sg.api.surveyresponse.list('39501')
```

By default, filters are cleared out after calls to the api. If you want to keep filters for the next call, set the `keep` parameter.

```python
sg.api.surveyresponse.list('39501', keep=True)
sg.api.surveyresponse.list('39502')
```

## API functions

Only a small subset of the API is currently unimplemented.

    TODO: Implement what's left.


## 0.2.0 Change notes

0.2.0 is a forwards incompatible release, but only minorly so.

Forwards incompatible changes:

- Renamed the 'change' operations to 'update'. This is consistent with SurveyGizmo's API naming.
- Removed the 'keep' kwarg for preserving filters bettween api funcion calls. This is now configured with 'preserve_filters'. Filters are now cleared manually with `api.clear_filters()`
- Removed the undocumented 'url_fetch' kwarg, which prevented api executioned and instead returned the prepared url.

Backwards incompatible changes:

- Modified 'api_version' to no longer has any effect on the client. SurveyGizmo provides no way to meaningfully differentiate between API versions, so this checking was unneeded and created code duplication
- Added 'prepare_url' as a replacement for 'url_fetch'. This forces the client to return the url after being prepared instead of executing the api call. This is useful in cases where you need to call the api asynchronously. 
- Added 'requests_kwargs'. These are additional arguments passed to `requests.get`. Useful for setting timeouts and otherwise configuring the requests library.


## Copyright & License
Copyright &copy; 2013 Ryan P Kilby. See LICENSE for details.

