- Third Version (add new theme in web app)
    I try to show proof of concept of loading new themes.
    I think I can add new features in the future task.

    You can see 'Add new themes' in top bar.
    When you click it, the program shows dialog with list of themes that are applied now and two file input field for adding new themes.

    1. Adding new themes
    You can select one of themes in the list and press add 'button'.
	After that you can see a new theme in solid menu in left side menu bar.

    2. Deleting themes
    You can see 'delete' button for each theme in the list.
    You can simply click 'delete' button and refresh the page manually.

    3. Prerequest
        I already configured for themes you gave me. So you don't have to do following things now.

        - You must copy theme html file in 'site_builder/static/static/elements/' directory and thumbnail image file in 'site_builder/static/static/elements/' directory.
        - Also, you should copy resource files(like css and js) into the project('site_builder\static\js', 'site_builder\static\css')
        - You have configure url for javascript, css and image files in theme html, css and js.


- Second Version
	I added new themes/templates into site builder site.
	You can see the new theme images in 'new theme images' folder.
	I added new themes in Headers, Content Sections, Portfolios, Team, Pricing Tables, Contact and Footers.

- First Version
	I implemented codecanyon-8432859-html-builder-frontend-version by using django

	1. Working Eviroment
	python2.7
	django1.9.2
	pycharm5.0.4

	2. Run
	It's a pycharm project, so you can test it in your local server by using pycharm

	3. Result.

	- Uploading files(images)
	- Preview page
	- Save htmls
		When exporting a site, the html pages are saved in sqlite database(tbl_html) and the program create zip file that contains 
