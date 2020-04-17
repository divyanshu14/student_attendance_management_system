import 'dart:async';
import 'dart:developer';

import 'package:sams/utils/user_info.dart';
import 'package:sams/utils/user_token.dart';
import 'package:sams/models/course.dart';
import 'package:sams/utils/network_util.dart';

class RestDatasource {
  static const BASE_URL = "http://192.168.43.132:8000/api/v1/db/";
  static const LOGIN_URL = BASE_URL + "login/";
  static const LIST_COURSES = BASE_URL + "list_courses/";
  static const _API_KEY = "somerandomkey";

  Future<bool> login(String username, String password) {
    return NetworkUtil.post(LOGIN_URL, 
    body: {
      "token": _API_KEY,
      "username": username,
      "password": password
    }
    ).then((dynamic res) {
      log('Response From $LOGIN_URL $res');
      UserToken.setToken(res["token"]);
      UserInfo.map(res["user_info"]);
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