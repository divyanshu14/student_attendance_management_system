import 'package:shared_preferences/shared_preferences.dart';
import 'package:sams/utils/constants.dart';

// User token is not a part of user as user data is dynamic and we only store token for mobile.
class UserToken {
  static String _token;
  static String get token =>_token;

  static Future<bool> fetchToken()async {
    final SharedPreferences _prefs = await SharedPreferences.getInstance() ;
    _token=_prefs.getString(Constants.TOKEN);
    return _token==null;
  }

  static Future <bool> setToken(String token) async{
    final SharedPreferences _prefs =await SharedPreferences.getInstance();
    bool set=await _prefs.setString(Constants.TOKEN, token);
    if(set){
      _token=token;
      return true;
    }  
    return false;
  }

}