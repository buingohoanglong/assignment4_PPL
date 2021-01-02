.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_3
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_1
	bastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	aload_1
	iconst_1
	aload_1
	iconst_0
	baload
	aload_1
	iconst_2
	baload
	iand
	bastore
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label2:
	aload_1
	iload_2
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label3:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label4
Label5:
Label1:
	return
.limit stack 14
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
