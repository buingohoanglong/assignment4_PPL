.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/foo()Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo()Ljava/lang/String;
Label0:
	ldc "Hello World"
	areturn
Label1:
	ldc ""
	areturn
.limit stack 3
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
