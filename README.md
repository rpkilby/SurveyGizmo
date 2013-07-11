
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

Currently, `user:pass` and `user:md5` are the only supported authentication methods. There is the `oauth_helper` module that is built on top of [rauth](https://github.com/litl/rauth), but it remains untested. You can try. *do it...*

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

* **api_version** - 'v3', 'head'. Defaults to 'head'
* **auth_method** - 'user:pass', 'user:md5', 'oauth'
* **username**
* **password**
* **md5_hash**
* **consumer_key**
* **consumer_secret**
* **access_token**
* **access_token_secret**
* **response_type** - None, 'json', 'pson', 'xml', 'debug'. If None, the response is returned as a python dictionary.

## Filters

Filters are currently untested. 

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


## Copyright & License
Copyright &copy; 2013 Ryan P Kilby. See LICENSE for details.

