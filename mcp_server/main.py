# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T08:56:23+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity
from fastapi import Path

from models import (
    Error,
    KeyDeleteResponse,
    KeyPKDeleteResponse,
    KeyPKGetResponse,
    KeyPKPostResponse,
    KeyPKPutResponse,
    KeyPostResponse,
    LoginPostResponse,
    ScopeJobDeleteResponse,
    ScopeJobGetResponse,
    ScopeJobPostResponse,
    ScopeJobPutResponse,
    ScopePostResponse,
)

app = MCPProxy(
    contact={
        'email': 'hello@authentiq.com',
        'name': 'Authentiq team',
        'url': 'http://authentiq.io/support',
    },
    description='Strong authentication, without the passwords.',
    license={
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html',
    },
    termsOfService='http://authentiq.com/terms/',
    title='Authentiq API',
    version='6',
    servers=[{'url': 'https://6-dot-authentiqio.appspot.com'}],
)


@app.delete(
    '/key',
    description=""" Revoke an Authentiq ID using email & phone.

If called with `email` and `phone` only, a verification code 
will be sent by email. Do a second call adding `code` to 
complete the revocation.
 """,
    tags=['push_notification_handling'],
)
def key_revoke_nosecret(email: str, phone: str = ..., code: Optional[str] = None):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/key',
    description=""" Register a new ID `JWT(sub, devtoken)`

v5: `JWT(sub, pk, devtoken, ...)`

See: https://github.com/skion/authentiq/wiki/JWT-Examples
 """,
    tags=[
        'key_lifecycle_management',
        'sign_request_handling',
        'push_notification_handling',
    ],
)
def key_register():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/key/{PK}',
    description=""" Revoke an Identity (Key) with a revocation secret """,
    tags=['key_lifecycle_management', 'sign_request_handling'],
)
def key_revoke(p_k: str = Path(..., alias='PK'), secret: str = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/key/{PK}',
    description=""" Get public details of an Authentiq ID.
 """,
    tags=['key_lifecycle_management'],
)
def key_retrieve(p_k: str = Path(..., alias='PK')):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.head(
    '/key/{PK}',
    description=""" HEAD info on Authentiq ID
 """,
    tags=['key_lifecycle_management'],
)
def head_key___p_k(p_k: str = Path(..., alias='PK')):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/key/{PK}',
    description=""" update properties of an Authentiq ID.
(not operational in v4; use PUT for now)

v5: POST issuer-signed email & phone scopes in
a self-signed JWT

See: https://github.com/skion/authentiq/wiki/JWT-Examples
 """,
    tags=['key_lifecycle_management'],
)
def key_update(p_k: str = Path(..., alias='PK')):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/key/{PK}',
    description=""" Update Authentiq ID by replacing the object.

v4: `JWT(sub,email,phone)` to bind email/phone hash; 

v5: POST issuer-signed email & phone scopes
and PUT to update registration `JWT(sub, pk, devtoken, ...)`

See: https://github.com/skion/authentiq/wiki/JWT-Examples
 """,
    tags=['key_lifecycle_management'],
)
def key_bind(p_k: str = Path(..., alias='PK')):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/login',
    description=""" push sign-in request
See: https://github.com/skion/authentiq/wiki/JWT-Examples
 """,
    tags=['sign_request_handling'],
)
def push_login_request(callback: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/scope',
    description=""" scope verification request
See: https://github.com/skion/authentiq/wiki/JWT-Examples
 """,
    tags=['key_lifecycle_management'],
)
def sign_request(test: Optional[int] = None):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/scope/{job}',
    description=""" delete a verification job """,
    tags=['sign_request_handling'],
)
def sign_delete(job: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/scope/{job}',
    description=""" get the status / current content of a verification job """,
    tags=['sign_request_handling'],
)
def sign_retrieve(job: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.head(
    '/scope/{job}',
    description=""" HEAD to get the status of a verification job """,
    tags=['sign_request_handling'],
)
def sign_retrieve_head(job: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/scope/{job}',
    description=""" this is a scope confirmation """,
    tags=['sign_request_handling'],
)
def sign_confirm(job: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/scope/{job}',
    description=""" authority updates a JWT with its signature
See: https://github.com/skion/authentiq/wiki/JWT-Examples
 """,
    tags=['sign_request_handling'],
)
def sign_update(job: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
