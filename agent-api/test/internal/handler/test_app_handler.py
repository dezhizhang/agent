import pytest
from pkg.response import HttpCode


class TestAppHandler:
    """app控制器的测试类"""

    @pytest.mark.parametrize("query",[None,"你好，你是谁"])
    def test_completion(self,query, client):
        resp = client.post("/app/completion", json={"query": "你好，你是?"})
        assert resp.status_code == 200
        if query is None:
            assert resp.json.get("code") == HttpCode.VALIDATION_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
