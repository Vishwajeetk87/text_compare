# text_compare

**Background**:
text_compare is a service which will compare given two input texts and return the Match count and Match score.

Match Count: common Subsequence between two texts
Match score: Score will range between 0 and 1 where 0 is no match and 1 will be the exact match.

The comparison logic makes use of Longest common subsequence algorithm to find the match.

Metric used for comparison is simple , score is calculated using formula  (length_of subsequence)/max(len_of_text1,len_of_text2)


**Running the Application**:

This application is using flask to create an endpoint ,the starting point for application is core.py simply execute following to start the app.

- python core.py

- URL for POST method : http://localhost/compare/ 
- Payload is in json format : -d '{"text1":"foo bar", "text2":"bar"}'

- Result
{
  Match Count : 1,
  Match Score : 0.5
 }
 
 - This application was tested using POSTMAN

Sample Curl
curl -X POST \
  http://127.0.0.1:5000/compare/ \
  -H 'content-type: application/json' \
  -d '{"text1":"foo bar", "text2":"bar"}'
