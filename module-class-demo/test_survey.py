from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    my_survey.store_response('English')
    assert my_survey.responses == ['English']
def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        my_survey.store_response(response)
    for response in responses:
        assert response in my_survey.responses