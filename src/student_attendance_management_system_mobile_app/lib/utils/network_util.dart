import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;

// TODO: implement custom exception handling for different status codes.

class NetworkUtil {
  // next three lines makes this class a Singleton
  // static NetworkUtil _instance = new NetworkUtil.internal();
  // NetworkUtil.internal();
  // factory NetworkUtil() => _instance;
 
  static final JsonDecoder _decoder = new JsonDecoder();

  static Future<dynamic> get(String url,{Map<String,String> headers} ) {
    return http.get(url,headers: headers).then((http.Response response) {
      final String responseBody = response.body;
      final int statusCode = response.statusCode;

      if (statusCode < 200 || statusCode >= 400 || json == null) {
        throw new Exception("Error while fetching data");
      }
      return _decoder.convert(responseBody);
    });
  }

  static Future<dynamic> post(String url, {Map headers, body, encoding}) {
    return http
        .post(url, body: body, headers: headers, encoding: encoding)
        .then((http.Response response) {
      final String responseBody = response.body;
      final int statusCode = response.statusCode;

      if (statusCode < 200 || statusCode >= 400 || json == null) {
        throw new Exception("Error while fetching data");
      }
      return _decoder.convert(responseBody);
    });
  }
}