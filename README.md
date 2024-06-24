# Boilit

boiler performance assessment

## Author

- **Manjunath Lakshman** - *Initial work* - [Email](mailto:manjunath.lakshman@bilfinger.com)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Requirements

This project requires Python 3.12 and Dash 2.17.1.


## Configure Tailwind 
On windows download the standalone tailwindcss cli executable. this helps to compile css without using node.js. The downloaded file for windows will be "tailwindcss-windows-x64.exe". Rename this to "tailwindcss.exe" and ensure it is added to the .gitignore.

Run the command 
tailwind -i ./assets/input.css -o ./assets/output.css --minify
