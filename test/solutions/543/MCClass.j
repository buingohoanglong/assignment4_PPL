.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_0
	putstatic MCClass/x I
Label0:
	invokestatic MCClass/foo()V
	getstatic MCClass/x I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo()V
Label0:
	iconst_1
	putstatic MCClass/x I
Label1:
	return
	return
.limit stack 2
.limit locals 0
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
