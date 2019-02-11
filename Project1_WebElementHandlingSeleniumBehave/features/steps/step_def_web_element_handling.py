#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given
from step_impl_web_element_handling import *


@given(u'Web element pop up example1 "{url}"')
def step_impl(context,url):
    web_element_pop_up_example1(url)


@given(u'Web element pop up example2 javascript "{url}"')
def step_impl(context,url):
    web_element_pop_up_example2_javascript(url)


@given(u'Web element form elements part1 "{url}"')
def step_impl(context,url):
    web_element_form_elements_part1(url)


@given(u'Web element window handling "{url}"')
def step_impl(context,url):
    web_element_window_handling(url)
