
import 'package:sams/models/student.dart';

import 'instructor.dart';

class Course{
  final String name;
  final String code;
  // final int lectureAttendance;
  // final int practicalAttendance;
  // final int tutoiralAttendace;
  List<Instructor> instructorsList;
  List<Student> studentList;
  List<Instructor> teachingAssistantList;

  Course({this.name,this.code});
  // Course({this.name,this.code,this.lectureAttendance,this.practicalAttendance,this.tutoiralAttendace});
}