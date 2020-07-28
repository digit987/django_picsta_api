# django_api_picsta
<i> An Instagram Like REST API in Django </i> <br>

<b> Dependencies </b> <br>
<i>
Djongo + MongoDB, djongo for MongoDB calls, 
check requirements.txt file for more details <br> 
APIView has been used for implementing REST functionalities. 
</i> <br>

<b> Models </b> <br>
<b> 1. User => Represents User Details with the following fields </b> <br>
<i>
('id',
'username',
'email',
'passwords',
'first_name',
'last_name',
'date_of_birth',
'created_on',
'log_in_history'
'bio',
'followers',
'following',
'comments') 
</i> <br>

<b> 2. Photo => Represents Photo Details with the following fields </b> <br>
<i>
'id' for Photo Id
'username' for Owner of the Photo
</i>

<b> 3. Posts => Represents Photo Details with the following fields </b> <br>
<i>
('id',
'username',
'timestamp',
'location',
'photo_id',
'tags',
'comments') 
</i> <br>

<b> Endpoints </b> <br>
<i>
path('users', views.UserView.as_view(), name="users"), <br>
path('users/<int:pk>', views.UserView.as_view(), name="users"), <br>
path('photos', views.PhotoView.as_view(), name="photos"), <br>
path('photos/<int:pk>', views.PhotoView.as_view(), name="photos"), <br>
path('posts', views.PostView.as_view(), name="post"), <br>
path('posts/<int:pk>', views.PostView.as_view(), name="posts") 
</i> <br>
