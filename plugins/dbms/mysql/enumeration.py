#!/usr/bin/env python

"""
$Id$

Copyright (c) 2006-2010 sqlmap developers (http://sqlmap.sourceforge.net/)
See the file 'doc/COPYING' for copying permission
"""

from lib.core.settings import DBMS
from plugins.generic.enumeration import Enumeration as GenericEnumeration

class Enumeration(GenericEnumeration):
    def __init__(self):
        GenericEnumeration.__init__(self, DBMS.MYSQL)
