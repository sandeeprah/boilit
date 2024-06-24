/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./boilit/pages/**/*.py", // scans all Python files in the pages directory
    "./boilit/components/**/*.py", // scans all Python files in the components directory
    "./boilit/app/**/*.py", // scans all Python files in the app directory
    "./boilit/app.py", // scans all Python files in the lib directory
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
