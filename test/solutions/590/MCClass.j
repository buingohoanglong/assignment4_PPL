.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static sqrt(F)F
.var 0 is x F from Label0 to Label1
Label0:
	ldc 1.1
	freturn
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static radius(FF)F
.var 0 is x F from Label0 to Label1
.var 1 is y F from Label0 to Label1
.var 2 is r F from Label0 to Label1
	ldc 5.5
	fstore_2
Label0:
	fload_0
	fload_0
	fmul
	fload_1
	fload_1
	fmul
	fadd
	invokestatic MCClass/sqrt(F)F
	fstore_2
	fload_2
	freturn
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
	ldc 3.5
	fstore_1
.var 2 is y F from Label0 to Label1
	ldc 4.6
	fstore_2
Label0:
	fload_1
	fload_2
	invokestatic MCClass/radius(FF)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 2
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
