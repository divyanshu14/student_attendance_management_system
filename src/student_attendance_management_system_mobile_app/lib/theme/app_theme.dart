import 'package:flutter/material.dart';

class AppTheme {
  AppTheme._();

  static const Color notWhite = Color(0xFFEDF0F2);
  static const Color nearlyWhite = Color(0xFFFDFE5);
  static const Color white = Color(0xFFFFFFFF);
  static const Color nearlyBlack = Color(0xFF213333);
  static const Color grey = Color(0xFF3A5160);
  static const Color dark_grey = Color(0xFF313A44);

  static const Color dark = Color(0xFF00A8CD);
  static const Color darker = Color(0xFF00899A);
  static const Color light =Color (0xFFD3EEE7);
  static const Color deactivatedText = Color(0xFFE6F4F1);
  static const Color overlay =Color(0x20006952);
  static const Color dismissibleBackground = Color(0xFF364A54);
  static const Color chipBackground = Color(0xFFEEF1F3);
  static const Color spacer = Color(0xFFF2F2F2);
  static const String fontName = 'WorkSans';

  static const Color primaryColor =Color(0xFF00A8CD);
  static const Color secondaryColor = Color(0xFFF46524);
  static ColorScheme colorScheme = const ColorScheme.light().copyWith(
    primary: primaryColor,
    secondary: secondaryColor,
  );


  static const TextTheme textTheme = TextTheme(
    display1: display1,
    headline: headline,
    title: title,
    subtitle: subtitle,
    body2: body2,
    body1: body1,
    caption: caption,
  );

  static const TextStyle display1 = TextStyle( // h4 -> display1
    fontFamily: fontName,
    fontWeight: FontWeight.bold,
    fontSize: 36,
    letterSpacing: 0.4,
    height: 0.9,
    color: darker,
  );

  static const TextStyle headline = TextStyle( // h5 -> headline
    fontFamily: fontName,
    fontWeight: FontWeight.bold,
    fontSize: 22,
    letterSpacing: 0.27,
    color: dark_grey,
  );

  static const TextStyle title = TextStyle( // h6 -> title
    fontFamily: fontName,
    fontWeight: FontWeight.bold,
    fontSize: 20,
    letterSpacing: 0.18,
    color: dark,
  );

  static const TextStyle subtitle = TextStyle( // subtitle2 -> subtitle
    fontFamily: fontName,
    fontWeight: FontWeight.w400,
    fontSize: 14,
    letterSpacing: -0.04,
    color: dark,
  );

  static const TextStyle body2 = TextStyle( // body1 -> body2
    fontFamily: fontName,
    fontWeight: FontWeight.w400,
    fontSize: 14,
    letterSpacing: 0.2,
    color: grey,
  );

  static const TextStyle body1 = TextStyle( // body2 -> body1
    fontFamily: fontName,
    fontWeight: FontWeight.w400,
    fontSize: 16,
    letterSpacing: -0.05,
    color: grey,
  );

  static const TextStyle caption = TextStyle( // Caption -> caption
    fontFamily: fontName,
    fontWeight: FontWeight.w400,
    fontSize: 12,
    letterSpacing: 0.2,
    color: white, // was white
  );

  static const TextStyle buttonText = TextStyle( 
    fontFamily: fontName,
    fontWeight: FontWeight.w400,
    fontSize: 20,
    letterSpacing: 0.2,
    color: white, // was white
  );

  static const TextStyle headlineLight =TextStyle(
    fontFamily: fontName,
    fontWeight: FontWeight.bold,
    fontSize: 26,
    letterSpacing: 0.27,
    color: white,
  );

  static const TextStyle displayLight = TextStyle( // h4 -> display1
    fontFamily: fontName,
    fontWeight: FontWeight.bold,
    fontSize: 36,
    letterSpacing: 0.4,
    height: 0.9,
    color: white,
  );
    static const TextStyle titleLight = TextStyle( // h6 -> title
    fontFamily: fontName,
    fontWeight: FontWeight.bold,
    fontSize: 20,
    letterSpacing: 0.18,
    color: white,
  );

  static TextTheme _buildTextTheme(TextTheme base) {
    const String fontName = 'Tondo';
    return base.copyWith(
      title: base.title.copyWith(fontFamily: fontName),
      body1: base.title.copyWith(fontFamily: fontName),
      body2: base.title.copyWith(fontFamily: fontName),
      button: base.title.copyWith(fontFamily: fontName),
      caption: base.title.copyWith(fontFamily: fontName),
      display1: base.title.copyWith(fontFamily: fontName),
      display2: base.title.copyWith(fontFamily: fontName),
      display3: base.title.copyWith(fontFamily: fontName),
      display4: base.title.copyWith(fontFamily: fontName),
      headline: base.title.copyWith(fontFamily: fontName),
      overline: base.title.copyWith(fontFamily: fontName),
      subhead: base.title.copyWith(fontFamily: fontName),
      subtitle: base.title.copyWith(fontFamily: fontName),
    );
  }

  static ThemeData buildLightTheme() {

    final ThemeData base = ThemeData.light();
    return base.copyWith(
      colorScheme: colorScheme,
      primaryColor: primaryColor,
      buttonColor: primaryColor,
      indicatorColor: Colors.white,
      splashColor: Colors.white24,
      splashFactory: InkRipple.splashFactory,
      accentColor: primaryColor,
      cardColor: Colors.white,
      canvasColor: Colors.white,
      backgroundColor: const Color(0xFFFFFEFA),
      scaffoldBackgroundColor: const Color(0xFFF6F6F6),
      errorColor: const Color(0xFFB00020),
      buttonTheme: ButtonThemeData(
        colorScheme: colorScheme,
        textTheme: ButtonTextTheme.primary,
      ),
      textTheme: _buildTextTheme(base.textTheme),
      primaryTextTheme: _buildTextTheme(base.primaryTextTheme),
      accentTextTheme: _buildTextTheme(base.accentTextTheme),
    );
  }



}
class HexColor extends Color {
  HexColor(final String hexColor) : super(_getColorFromHex(hexColor));
  static int _getColorFromHex(String hexColor) {
    hexColor = hexColor.toUpperCase().replaceAll('#', '');
    if (hexColor.length == 6) {
      hexColor = 'FF' + hexColor;
    }
    return int.parse(hexColor, radix: 16);
  }
}