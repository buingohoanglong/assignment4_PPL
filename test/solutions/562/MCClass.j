.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [F

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
	putstatic MCClass/x [F
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 4.4
	fastore
	dup
	iconst_1
	ldc 5.5
	fastore
	dup
	iconst_2
	ldc 6.6
	fastore
	putstatic MCClass/x [F
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label2:
	getstatic MCClass/x [F
	iload_1
	getstatic MCClass/x [F
	iload_1
	faload
	ldc 2.0
	fmul
	ldc 1.0
	fadd
	fastore
Label3:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label4
Label5:
	iconst_0
	istore_1
Label10:
	iload_1
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
Label8:
	getstatic MCClass/x [F
	iload_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label9:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label10
Label11:
Label1:
	return
.limit stack 13
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
