.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
Label0:
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
.var 2 is x F from Label2 to Label3
	ldc 1.5
	fstore_2
Label2:
	fload_2
	ldc 1.5
	fadd
	fstore_2
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label3:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label4
Label5:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 8
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
