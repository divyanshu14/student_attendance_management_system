import 'dart:async';
import 'dart:developer';

// import 'package:sams/utils/user_info.dart';
import 'package:sams/utils/user_token.dart';
import 'package:sams/models/course.dart';
import 'package:sams/utils/network_util.dart';

class RestDatasource {
  static const BASE_URL = "http://192.168.60.132:8000/db_api/";
  static const LOGIN_URL = BASE_URL + "api_token_auth/";
  static const LIST_COURSES = BASE_URL + "list_courses/";
  static const _API_KEY = "somerandomkey";

  Future<bool> login(String email, String password) {
    log(LOGIN_URL);
    return NetworkUtil.post(LOGIN_URL, 
    body: {
      "token": _API_KEY,
      "email": email,
      "password": password
    }
    ).then((dynamic res) {
      log('Response From $LOGIN_URL $res');
      UserToken.setToken(res["token"]);
    })
    .catchError((error){
      throw (error);
    })
    ;
  }

  Future<Course> listCourses(String token){
    return NetworkUtil.get(LIST_COURSES,
    headers: {
      "authorisation": token,
    }
    );
  }



}