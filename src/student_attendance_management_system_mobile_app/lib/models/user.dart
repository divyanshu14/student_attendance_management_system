class User {

  final String _email;
  final String _firstName;
  final String _lastName;
//   final bool _isAdmin;
//   final bool _isStudent;
//   final bool _isInstructor;
//   final bool _isTeachingAssistant;


//   User(this._email,this._firstName,this._lastName,this._isAdmin, this._isStudent, this._isTeachingAssistant, this._isInstructor);
  User(this._email,this._firstName,this._lastName);

  factory User.fromJson(dynamic userObject) {

    return User(
      userObject["email"],
      userObject["first_name"],
      userObject["last_name"],
    );
  } 


//   String get username => _email;
//   String get firstName => _firstName;
//   String get lastName => _lastName;
//   bool get adminPermissions => _isAdmin;
//   bool get isTA => _isTeachingAssistant;
//   bool get isTeacher => _isInstructor;
//   bool get isStudent => _isStudent;

}