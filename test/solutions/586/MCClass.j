.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	astore_1
.var 2 is y Ljava/lang/String; from Label0 to Label1
	ldc "World"
	astore_2
Label0:
	aload_1
	astore_2
	aload_1
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
	return
.limit stack 3
.limit locals 3
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
