.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
.var 2 is y I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iload_1
	iload_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	iload_1
	iload_2
	idiv
	iconst_1
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label2
Label10:
	ldc "Hello"
	invokestatic io/print(Ljava/lang/String;)V
Label11:
	goto Label3
Label2:
Label12:
	ldc "World"
	invokestatic io/print(Ljava/lang/String;)V
Label13:
Label3:
Label1:
	return
.limit stack 9
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
