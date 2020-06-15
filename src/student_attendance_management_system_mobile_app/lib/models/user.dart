import 'package:sams/models/classevent_coordinator.dart';

class User {
  String firstName;
  String lastName;
  String email;
  ClasseventCoordinator classeventcoordinator;

  User({this.firstName, this.lastName, this.email, this.classeventcoordinator});

  User.fromJson(Map<String, dynamic> json) {
    firstName = json['first_name'];
    lastName = json['last_name'];
    email = json['email'];
    classeventcoordinator = json['classeventcoordinator'] != null
        ? new ClasseventCoordinator.fromJson(json['classeventcoordinator'])
        : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['first_name'] = this.firstName;
    data['last_name'] = this.lastName;
    data['email'] = this.email;
    if (this.classeventcoordinator != null) {
      data['classeventcoordinator'] = this.classeventcoordinator.toJson();
    }
    return data;
  }
}
