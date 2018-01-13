"""
"""

# Created on 2016.08.31
#
# Author: Giovanni Cannata
#
# Copyright 2014 - 2018 Giovanni Cannata
#
# This file is part of ldap3.
#
# ldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.


# result codes
RESULT_SUCCESS = 0
RESULT_OPERATIONS_ERROR = 1
RESULT_PROTOCOL_ERROR = 2
RESULT_TIME_LIMIT_EXCEEDED = 3
RESULT_SIZE_LIMIT_EXCEEDED = 4
RESULT_COMPARE_FALSE = 5
RESULT_COMPARE_TRUE = 6
RESULT_AUTH_METHOD_NOT_SUPPORTED = 7
RESULT_STRONGER_AUTH_REQUIRED = 8
RESULT_RESERVED = 9
RESULT_REFERRAL = 10
RESULT_ADMIN_LIMIT_EXCEEDED = 11
RESULT_UNAVAILABLE_CRITICAL_EXTENSION = 12
RESULT_CONFIDENTIALITY_REQUIRED = 13
RESULT_SASL_BIND_IN_PROGRESS = 14
RESULT_NO_SUCH_ATTRIBUTE = 16
RESULT_UNDEFINED_ATTRIBUTE_TYPE = 17
RESULT_INAPPROPRIATE_MATCHING = 18
RESULT_CONSTRAINT_VIOLATION = 19
RESULT_ATTRIBUTE_OR_VALUE_EXISTS = 20
RESULT_INVALID_ATTRIBUTE_SYNTAX = 21
RESULT_NO_SUCH_OBJECT = 32
RESULT_ALIAS_PROBLEM = 33
RESULT_INVALID_DN_SYNTAX = 34
RESULT_ALIAS_DEREFERENCING_PROBLEM = 36
RESULT_INAPPROPRIATE_AUTHENTICATION = 48
RESULT_INVALID_CREDENTIALS = 49
RESULT_INSUFFICIENT_ACCESS_RIGHTS = 50
RESULT_BUSY = 51
RESULT_UNAVAILABLE = 52
RESULT_UNWILLING_TO_PERFORM = 53
RESULT_LOOP_DETECTED = 54
RESULT_NAMING_VIOLATION = 64
RESULT_OBJECT_CLASS_VIOLATION = 65
RESULT_NOT_ALLOWED_ON_NON_LEAF = 66
RESULT_NOT_ALLOWED_ON_RDN = 67
RESULT_ENTRY_ALREADY_EXISTS = 68
RESULT_OBJECT_CLASS_MODS_PROHIBITED = 69
RESULT_AFFECT_MULTIPLE_DSAS = 71
RESULT_OTHER = 80
RESULT_LCUP_RESOURCES_EXHAUSTED = 113
RESULT_LCUP_SECURITY_VIOLATION = 114
RESULT_LCUP_INVALID_DATA = 115
RESULT_LCUP_UNSUPPORTED_SCHEME = 116
RESULT_LCUP_RELOAD_REQUIRED = 117
RESULT_CANCELED = 118
RESULT_NO_SUCH_OPERATION = 119
RESULT_TOO_LATE = 120
RESULT_CANNOT_CANCEL = 121
RESULT_ASSERTION_FAILED = 122
RESULT_AUTHORIZATION_DENIED = 123
RESULT_E_SYNC_REFRESH_REQUIRED = 4096

RESULT_CODES = {
    RESULT_SUCCESS: 'success',
    RESULT_OPERATIONS_ERROR: 'operationsError',
    RESULT_PROTOCOL_ERROR: 'protocolError',
    RESULT_TIME_LIMIT_EXCEEDED: 'timeLimitExceeded',
    RESULT_SIZE_LIMIT_EXCEEDED: 'sizeLimitExceeded',
    RESULT_COMPARE_FALSE: 'compareFalse',
    RESULT_COMPARE_TRUE: 'compareTrue',
    RESULT_AUTH_METHOD_NOT_SUPPORTED: 'authMethodNotSupported',
    RESULT_RESERVED: 'reserved',
    RESULT_STRONGER_AUTH_REQUIRED: 'strongerAuthRequired',
    RESULT_REFERRAL: 'referral',
    RESULT_ADMIN_LIMIT_EXCEEDED: 'adminLimitExceeded',
    RESULT_UNAVAILABLE_CRITICAL_EXTENSION: 'unavailableCriticalExtension',
    RESULT_CONFIDENTIALITY_REQUIRED: 'confidentialityRequired',
    RESULT_SASL_BIND_IN_PROGRESS: 'saslBindInProgress',
    RESULT_NO_SUCH_ATTRIBUTE: 'noSuchAttribute',
    RESULT_UNDEFINED_ATTRIBUTE_TYPE: 'undefinedAttributeType',
    RESULT_INAPPROPRIATE_MATCHING: 'inappropriateMatching',
    RESULT_CONSTRAINT_VIOLATION: 'constraintViolation',
    RESULT_ATTRIBUTE_OR_VALUE_EXISTS: 'attributeOrValueExists',
    RESULT_INVALID_ATTRIBUTE_SYNTAX: 'invalidAttributeSyntax',
    RESULT_NO_SUCH_OBJECT: 'noSuchObject',
    RESULT_ALIAS_PROBLEM: 'aliasProblem',
    RESULT_INVALID_DN_SYNTAX: 'invalidDNSyntax',
    RESULT_ALIAS_DEREFERENCING_PROBLEM: 'aliasDereferencingProblem',
    RESULT_INAPPROPRIATE_AUTHENTICATION: 'inappropriateAuthentication',
    RESULT_INVALID_CREDENTIALS: 'invalidCredentials',
    RESULT_INSUFFICIENT_ACCESS_RIGHTS: 'insufficientAccessRights',
    RESULT_BUSY: 'busy',
    RESULT_UNAVAILABLE: 'unavailable',
    RESULT_UNWILLING_TO_PERFORM: 'unwillingToPerform',
    RESULT_LOOP_DETECTED: 'loopDetected',
    RESULT_NAMING_VIOLATION: 'namingViolation',
    RESULT_OBJECT_CLASS_VIOLATION: 'objectClassViolation',
    RESULT_NOT_ALLOWED_ON_NON_LEAF: 'notAllowedOnNonLeaf',
    RESULT_NOT_ALLOWED_ON_RDN: 'notAllowedOnRDN',
    RESULT_ENTRY_ALREADY_EXISTS: 'entryAlreadyExists',
    RESULT_OBJECT_CLASS_MODS_PROHIBITED: 'objectClassModsProhibited',
    RESULT_AFFECT_MULTIPLE_DSAS: 'affectMultipleDSAs',
    RESULT_OTHER: 'other',
    RESULT_LCUP_RESOURCES_EXHAUSTED: 'lcupResourcesExhausted',
    RESULT_LCUP_SECURITY_VIOLATION: 'lcupSecurityViolation',
    RESULT_LCUP_INVALID_DATA: 'lcupInvalidData',
    RESULT_LCUP_UNSUPPORTED_SCHEME: 'lcupUnsupportedScheme',
    RESULT_LCUP_RELOAD_REQUIRED: 'lcupReloadRequired',
    RESULT_CANCELED: 'canceled',
    RESULT_NO_SUCH_OPERATION: 'noSuchOperation',
    RESULT_TOO_LATE: 'tooLate',
    RESULT_CANNOT_CANCEL: 'cannotCancel',
    RESULT_ASSERTION_FAILED: 'assertionFailed',
    RESULT_AUTHORIZATION_DENIED: 'authorizationDenied',
    RESULT_E_SYNC_REFRESH_REQUIRED: 'e-syncRefreshRequired'
}

# do not raise exception for (in raise_exceptions connection mode)
DO_NOT_RAISE_EXCEPTIONS = [RESULT_SUCCESS, RESULT_COMPARE_FALSE, RESULT_COMPARE_TRUE, RESULT_REFERRAL, RESULT_SASL_BIND_IN_PROGRESS]
