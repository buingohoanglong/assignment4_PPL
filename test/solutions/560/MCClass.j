.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 1.1
	fastore
	dup
	iconst_1
	ldc 2.2
	fastore
	dup
	iconst_2
	ldc 3.3
	fastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	aload_1
	iconst_1
	aload_1
	iconst_0
	faload
	aload_1
	iconst_2
	faload
	fadd
	fastore
	iconst_0
	istore_2
Label2:
	iload_2
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	aload_1
	iload_2
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label3:
Label4:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label2
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
