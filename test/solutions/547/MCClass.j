.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
	ldc 1.5
	fstore_1
.var 2 is b F from Label0 to Label1
	ldc 2.0
	fstore_2
Label0:
	fload_1
	fload_2
	invokestatic MCClass/foo(FF)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
	return
.limit stack 4
.limit locals 3
.end method

.method public static sum(FF)F
.var 0 is x F from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
	fload_0
	fload_1
	fadd
	freturn
Label1:
	ldc 0.0
	freturn
.limit stack 2
.limit locals 2
.end method

.method public static foo(FF)F
.var 0 is x F from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
	fload_0
	fload_1
	invokestatic MCClass/sum(FF)F
	freturn
Label1:
	ldc 0.0
	freturn
.limit stack 2
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
