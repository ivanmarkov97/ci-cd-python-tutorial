from src.database.operations import select


def test_db_operation_select(mocker):
    mock_result = [
        {"item_id": 1, "price": 100, "name": "Item 1"},
        {"item_id": 2, "price": 200, "name": "Item 2"},
        {"item_id": 3, "price": 300, "name": "Item 3"},
    ]

    db_config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "root",
        "db": "test_db",
    }
    sql = "select * from items"

    mock_object = mocker.patch(
        "src.database.operations.create_db_response", return_value=mock_result
    )

    db_result = select(db_config, sql)
    item_keys = db_result[0].keys()
    assert len(db_result) == 3
    assert "item_id" in item_keys
    assert "price" in item_keys
    assert "name" in item_keys
    assert mock_object.call_count == 1
    assert mock_object.call_args_list[0][0][0] == db_config
    assert mock_object.call_args_list[0][0][1] == sql
