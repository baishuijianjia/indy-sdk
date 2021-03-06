from indy import ledger

import json
import pytest


@pytest.mark.asyncio
async def test_build_get_revoc_reg_delta_request_work():
    identifier = "Th7MpTaRZVRYnPiabds81Y"

    rev_reg_def_id = "NcYxiDXkpYi6ov5FcYDi1e:4:NcYxiDXkpYi6ov5FcYDi1e:3:CL:1:CL_ACCUM:TAG_1"
    to = 100

    expected_response = {
        "operation": {
            "type": "117",
            "revocRegDefId": rev_reg_def_id,
            "to": to
        }
    }

    request = json.loads(await ledger.build_get_revoc_reg_delta_request(identifier, rev_reg_def_id, None, to))
    assert expected_response.items() <= request.items()
