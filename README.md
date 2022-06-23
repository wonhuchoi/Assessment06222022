Instructions:
    - I have made the applciation into a docker application. This is to remove any issues people may have with python packages

    - To run the application
        1. clone this repo
        2. Navigate to the root directory
        3. Run ``` docker build -t *your_image_name* Dockerfile . ```
        4. Run ``` docker run -p 8081:8081 *your_image_name* ```
        5. send requests to the endpoint (this example runs on localhost:8081/generate-token)
    
    **Note: only the post method has been implemented as per the assesment requirements**

## Testing

- The given test cases were added, as well as a few others. They can be run from the root directory, by running 
``` python3 -m unittest test.py ```

## Considerations

- No authentication was added as I believed it to be out of the scope of the project, but could be added as well

## References and docuemntation

- The following library was used for generating the hmac token https://docs.python.org/3/library/hmac.html
