import pytest
from app import app
from dal.database import get_db
from dal.repositories import QuestionRepository
from huggingface_hub import InferenceClient


@pytest.fixture
def client():
    app.config['Testing'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code is 200


def test_ask_question(client, mocker):
    # Patch the specific OpenAI API-like structure used in app.py
    mock_client = mocker.patch('app.client')
    mock_create = mock_client.chat.completions.create
    mock_create.return_value = mocker.Mock(choices=[mocker.Mock(message=mocker.Mock(content='Mocked answer'))])

    # Configure mock_db for context management
    mock_db = mocker.MagicMock()
    mock_db.__enter__.return_value = mocker.Mock()
    mock_db.__exit__.return_value = None
    mocker.patch('app.get_db', return_value=mock_db)

    # Mock repository
    mock_repo = mocker.Mock()
    mock_repo.create_question.return_value = mocker.Mock(id=1, question='Test question', answer='Mocked answer')
    mocker.patch('app.QuestionRepository', return_value=mock_repo)

    # Perform the POST request
    response = client.post('/ask', json={'question': 'Test question'})
    assert response.status_code == 200
    assert response.json['question'] == 'Test question'
    assert response.json['answer'] == 'Mocked answer'






