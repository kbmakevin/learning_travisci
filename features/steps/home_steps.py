from behave import *

"""Translates the home scenarios into python code
"""

@when(u'I navigate to Home Page')
def step_impl(ctx):
    ctx.resp = ctx.client.get('/')

@then(u'Home Page should be displayed')
def step_impl(ctx):
    assert 'Home Page' in ctx.resp
