.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Hello"
	aastore
	dup
	iconst_1
	ldc "World"
	aastore
	dup
	iconst_2
	ldc "!"
	aastore
	astore_1
Label0:
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "I"
	aastore
	dup
	iconst_1
	ldc "am"
	aastore
	dup
	iconst_2
	ldc "Long"
	aastore
	astore_1
	aload_1
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
	return
.limit stack 10
.limit locals 2
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
