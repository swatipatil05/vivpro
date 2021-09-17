##Prerequisites 
# install Django  -> pip install django
# install djangorestframework -> pip install djangorestframework
# or follow the below steps

## Running application in Windows-local browser.
1. Download the project.
2. Change directory where manage.py resides. 
3. Prerequisites: pip freeze > requirements.txt
4. Run command python manage.py runserver, it will give you the local address to run the application 
   (eg http://127.0.0.1:8000/) 
5. Click on this eg http://127.0.0.1:8000/, you will see all the API lists on the browser.
6. API List:
   a. populate_data/   -> this API is used to insert all the data from input JSON into Song table.
	 (GET API ) http://127.0.0.1:8000/populate_data/
	  
   b. songs/    -> this API will show all the songs from the table Song with the pagination.
	  (GET API ) http://127.0.0.1:8000/songs/  :  this will give the fields from Song table along with the next &
	                                              previous page number , each page is showing 10 items
	 
	  
	  For pagination : 
	  (GET API ) http://127.0.0.1:8000/songs/?page=2 : this will give the page 2 data 
	  
	  
	  Search for given title :
	  (GET API)  http://127.0.0.1:8000/songs/?title=all :  Search for the title , this will give the fields from Song table along with the next & previus page number, each page is showing 10 items
   
   c. Rate the given song
	  rate_song/<int:pk>  ->  Rate the song with primary key(pk), start_rating as a json input.
	  (PUT API) http://127.0.0.1:8000/rate_song/1    {"pk": 1, "start_rating": 5}
		
       
   