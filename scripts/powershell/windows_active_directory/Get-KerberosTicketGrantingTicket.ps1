function Get-KerberosTicketGrantingTicket
{
    <#
    .SYNOPSIS

    Gets the Kerberos Tickets Granting Tickets from all Logon Sessions

    .DESCRIPTION

    Get-KerberosTicketGrantingTicket uses the Local Security Authority (LSA) functions to enumerate Kerberos logon sessions and return their associate Kerberos Ticket Granting Tickets.

    .NOTES

    Author: Jared Atkinson (@jaredcatkinson)
    License: BSD 3-Clause
    Required Dependencies: None
    Optional Dependencies: None

    .EXAMPLE
    
    Get-KerberosTicketGrantingTicket

    ServiceName                  : krbtgt
    ClientName                   : mwright_a
    DomainName                   : CITADEL.COVERTIUS.LOCAL
    TargetDomainName             : CITADEL.COVERTIUS.LOCAL
    AltTargetDomainName          : CITADEL.COVERTIUS.LOCAL
    SessionKeyType               : aes256_cts_hmac_sha1_96
    SessionKey                   : {51, 7, 83, 44...}
    TicketFlags                  : name_canonicalize, pre_authent, initial, renewable, forwardable
    KeyExpirationTime            : 1/1/1601 1:00:00 AM
    StartTime                    : 9/20/2017 3:27:59 PM
    EndTime                      : 9/21/2017 1:27:59 AM
    RenewUntil                   : 9/26/2017 7:57:57 PM
    TimeSkew                     : 0
    EncodedTicketSize            : 1141
    EncodedTicket                : {97, 130, 4, 113...}
    SessionLogonId               : 11965821
    SessionUserName              : john
    SessionUserPrincipalName     : 
    SessionLogonType             : NewCredentials
    SessionAuthenticationPackage : Negotiate
    SessionLogonServer           : 

    ServiceName                  : krbtgt
    ClientName                   : bharris_da
    DomainName                   : citadel.covertius.local
    TargetDomainName             : citadel.covertius.local
    AltTargetDomainName          : citadel.covertius.local
    SessionKeyType               : rc4_hmac
    SessionKey                   : {19, 216, 233, 89...}
    TicketFlags                  : pre_authent, initial, renewable, forwardable
    KeyExpirationTime            : 1/1/1601 1:00:00 AM
    StartTime                    : 9/20/2017 6:52:16 PM
    EndTime                      : 9/18/2027 6:52:16 PM
    RenewUntil                   : 9/18/2027 6:52:16 PM
    TimeSkew                     : 0
    EncodedTicketSize            : 1040
    EncodedTicket                : {97, 130, 4, 12...}
    SessionLogonId               : 11782805
    SessionUserName              : john
    SessionUserPrincipalName     : 
    SessionLogonType             : Interactive
    SessionAuthenticationPackage : NTLM
    SessionLogonServer           : ACHILLES

    ServiceName                  : krbtgt
    ClientName                   : mwright_a
    DomainName                   : CITADEL.COVERTIUS.LOCAL
    TargetDomainName             : CITADEL.COVERTIUS.LOCAL
    AltTargetDomainName          : CITADEL.COVERTIUS.LOCAL
    SessionKeyType               : aes256_cts_hmac_sha1_96
    SessionKey                   : {226, 202, 146, 183...}
    TicketFlags                  : name_canonicalize, pre_authent, initial, 
                                   renewable, forwardable
    KeyExpirationTime            : 1/1/1601 1:00:00 AM
    StartTime                    : 9/20/2017 9:28:39 PM
    EndTime                      : 9/21/2017 7:28:39 AM
    RenewUntil                   : 9/25/2017 8:43:33 PM
    TimeSkew                     : 0
    EncodedTicketSize            : 1141
    EncodedTicket                : {97, 130, 4, 113...}
    SessionLogonId               : 5302852
    SessionUserName              : mwright_a
    SessionUserPrincipalName     : mwright_a@citadel.covertius.local
    SessionLogonType             : Interactive
    SessionAuthenticationPackage : Negotiate
    SessionLogonServer           : zeus

    ServiceName                  : krbtgt
    ClientName                   : mwright_a
    DomainName                   : CITADEL.COVERTIUS.LOCAL
    TargetDomainName             : CITADEL.COVERTIUS.LOCAL
    AltTargetDomainName          : CITADEL.COVERTIUS.LOCAL
    SessionKeyType               : aes256_cts_hmac_sha1_96
    SessionKey                   : {128, 59, 86, 81...}
    TicketFlags                  : name_canonicalize, pre_authent, initial, 
                                   renewable, forwardable
    KeyExpirationTime            : 1/1/1601 1:00:00 AM
    StartTime                    : 9/20/2017 9:28:38 PM
    EndTime                      : 9/21/2017 7:28:38 AM
    RenewUntil                   : 9/25/2017 8:43:33 PM
    TimeSkew                     : 0
    EncodedTicketSize            : 1141
    EncodedTicket                : {97, 130, 4, 113...}
    SessionLogonId               : 5302821
    SessionUserName              : mwright_a
    SessionUserPrincipalName     : mwright_a@citadel.covertius.local
    SessionLogonType             : Interactive
    SessionAuthenticationPackage : Kerberos
    SessionLogonServer           : zeus

    ServiceName                  : krbtgt
    ClientName                   : amurphy
    DomainName                   : CITADEL.COVERTIUS.LOCAL
    TargetDomainName             : CITADEL.COVERTIUS.LOCAL
    AltTargetDomainName          : CITADEL.COVERTIUS.LOCAL
    SessionKeyType               : aes256_cts_hmac_sha1_96
    SessionKey                   : {96, 147, 44, 57...}
    TicketFlags                  : name_canonicalize, pre_authent, initial, 
                                   renewable, forwardable
    KeyExpirationTime            : 1/1/1601 1:00:00 AM
    StartTime                    : 9/20/2017 8:39:36 PM
    EndTime                      : 9/21/2017 6:39:36 AM
    RenewUntil                   : 9/26/2017 3:24:32 PM
    TimeSkew                     : 0
    EncodedTicketSize            : 1107
    EncodedTicket                : {97, 130, 4, 79...}
    SessionLogonId               : 5092111
    SessionUserName              : amurphy
    SessionUserPrincipalName     : amurphy@citadel.covertius.local
    SessionLogonType             : RemoteInteractive
    SessionAuthenticationPackage : Kerberos
    SessionLogonServer           : zeus

    ServiceName                  : krbtgt
    ClientName                   : ACHILLES$
    DomainName                   : CITADEL.COVERTIUS.LOCAL
    TargetDomainName             : CITADEL.COVERTIUS.LOCAL
    AltTargetDomainName          : CITADEL.COVERTIUS.LOCAL
    SessionKeyType               : aes256_cts_hmac_sha1_96
    SessionKey                   : {108, 229, 243, 155...}
    TicketFlags                  : name_canonicalize, pre_authent, initial, 
                                   renewable, forwardable
    KeyExpirationTime            : 1/1/1601 1:00:00 AM
    StartTime                    : 9/20/2017 3:04:46 PM
    EndTime                      : 9/21/2017 1:04:46 AM
    RenewUntil                   : 9/24/2017 8:34:27 PM
    TimeSkew                     : 0
    EncodedTicketSize            : 1133
    EncodedTicket                : {97, 130, 4, 105...}
    SessionLogonId               : 996
    SessionUserName              : ACHILLES$
    SessionUserPrincipalName     : ACHILLES$@citadel.covertius.local
    SessionLogonType             : Service
    SessionAuthenticationPackage : Negotiate
    SessionLogonServer           : 

    ServiceName                  : krbtgt
    ClientName                   : ACHILLES$
    DomainName                   : CITADEL.COVERTIUS.LOCAL
    TargetDomainName             : CITADEL.COVERTIUS.LOCAL
    AltTargetDomainName          : CITADEL.COVERTIUS.LOCAL
    SessionKeyType               : aes256_cts_hmac_sha1_96
    SessionKey                   : {151, 61, 31, 170...}
    TicketFlags                  : name_canonicalize, pre_authent, initial, 
                                   renewable, forwardable
    KeyExpirationTime            : 1/1/1601 1:00:00 AM
    StartTime                    : 9/20/2017 4:13:23 PM
    EndTime                      : 9/21/2017 2:13:23 AM
    RenewUntil                   : 9/24/2017 8:34:27 PM
    TimeSkew                     : 0
    EncodedTicketSize            : 1133
    EncodedTicket                : {97, 130, 4, 105...}
    SessionLogonId               : 999
    SessionUserName              : ACHILLES$
    SessionUserPrincipalName     : ACHILLES$@citadel.covertius.local
    SessionLogonType             : 
    SessionAuthenticationPackage : Negotiate
    SessionLogonServer           : 
    #>
    
    [CmdletBinding()]
    param
    (

    )

    #region PSReflect
    function New-InMemoryModule
    {
    <#
    .SYNOPSIS

    Creates an in-memory assembly and module

    Author: Matthew Graeber (@mattifestation)
    License: BSD 3-Clause
    Required Dependencies: None
    Optional Dependencies: None
 
    .DESCRIPTION

    When defining custom enums, structs, and unmanaged functions, it is
    necessary to associate to an assembly module. This helper function
    creates an in-memory module that can be passed to the 'enum',
    'struct', and Add-Win32Type functions.

    .PARAMETER ModuleName

    Specifies the desired name for the in-memory assembly and module. If
    ModuleName is not provided, it will default to a GUID.

    .EXAMPLE

    $Module = New-InMemoryModule -ModuleName Win32
    #>

        Param
        (
            [Parameter(Position = 0)]
            [ValidateNotNullOrEmpty()]
            [String]
            $ModuleName = [Guid]::NewGuid().ToString()
        )

        $AppDomain = [Reflection.Assembly].Assembly.GetType('System.AppDomain').GetProperty('CurrentDomain').GetValue($null, @())
        $LoadedAssemblies = $AppDomain.GetAssemblies()

        foreach ($Assembly in $LoadedAssemblies) {
            if ($Assembly.FullName -and ($Assembly.FullName.Split(',')[0] -eq $ModuleName)) {
                return $Assembly
            }
        }

        $DynAssembly = New-Object Reflection.AssemblyName($ModuleName)
        $Domain = $AppDomain
        $AssemblyBuilder = $Domain.DefineDynamicAssembly($DynAssembly, 'Run')
        $ModuleBuilder = $AssemblyBuilder.DefineDynamicModule($ModuleName, $False)

        return $ModuleBuilder
    }

    # A helper function used to reduce typing while defining function
    # prototypes for Add-Win32Type.
    function func
    {
        Param
        (
            [Parameter(Position = 0, Mandatory = $True)]
            [String]
            $DllName,

            [Parameter(Position = 1, Mandatory = $True)]
            [string]
            $FunctionName,

            [Parameter(Position = 2, Mandatory = $True)]
            [Type]
            $ReturnType,

            [Parameter(Position = 3)]
            [Type[]]
            $ParameterTypes,

            [Parameter(Position = 4)]
            [Runtime.InteropServices.CallingConvention]
            $NativeCallingConvention,

            [Parameter(Position = 5)]
            [Runtime.InteropServices.CharSet]
            $Charset,

            [String]
            $EntryPoint,

            [Switch]
            $SetLastError
        )

        $Properties = @{
            DllName = $DllName
            FunctionName = $FunctionName
            ReturnType = $ReturnType
        }

        if ($ParameterTypes) { $Properties['ParameterTypes'] = $ParameterTypes }
        if ($NativeCallingConvention) { $Properties['NativeCallingConvention'] = $NativeCallingConvention }
        if ($Charset) { $Properties['Charset'] = $Charset }
        if ($SetLastError) { $Properties['SetLastError'] = $SetLastError }
        if ($EntryPoint) { $Properties['EntryPoint'] = $EntryPoint }

        New-Object PSObject -Property $Properties
    }

    function Add-Win32Type
    {
    <#
    .SYNOPSIS

    Creates a .NET type for an unmanaged Win32 function.

    Author: Matthew Graeber (@mattifestation)
    License: BSD 3-Clause
    Required Dependencies: None
    Optional Dependencies: func
 
    .DESCRIPTION

    Add-Win32Type enables you to easily interact with unmanaged (i.e.
    Win32 unmanaged) functions in PowerShell. After providing
    Add-Win32Type with a function signature, a .NET type is created
    using reflection (i.e. csc.exe is never called like with Add-Type).

    The 'func' helper function can be used to reduce typing when defining
    multiple function definitions.

    .PARAMETER DllName

    The name of the DLL.

    .PARAMETER FunctionName

    The name of the target function.

    .PARAMETER EntryPoint

    The DLL export function name. This argument should be specified if the
    specified function name is different than the name of the exported
    function.

    .PARAMETER ReturnType

    The return type of the function.

    .PARAMETER ParameterTypes

    The function parameters.

    .PARAMETER NativeCallingConvention

    Specifies the native calling convention of the function. Defaults to
    stdcall.

    .PARAMETER Charset

    If you need to explicitly call an 'A' or 'W' Win32 function, you can
    specify the character set.

    .PARAMETER SetLastError

    Indicates whether the callee calls the SetLastError Win32 API
    function before returning from the attributed method.

    .PARAMETER Module

    The in-memory module that will host the functions. Use
    New-InMemoryModule to define an in-memory module.

    .PARAMETER Namespace

    An optional namespace to prepend to the type. Add-Win32Type defaults
    to a namespace consisting only of the name of the DLL.

    .EXAMPLE

    $Mod = New-InMemoryModule -ModuleName Win32

    $FunctionDefinitions = @(
      (func kernel32 GetProcAddress ([IntPtr]) @([IntPtr], [String]) -Charset Ansi -SetLastError),
      (func kernel32 GetModuleHandle ([Intptr]) @([String]) -SetLastError),
      (func ntdll RtlGetCurrentPeb ([IntPtr]) @())
    )

    $Types = $FunctionDefinitions | Add-Win32Type -Module $Mod -Namespace 'Win32'
    $Kernel32 = $Types['kernel32']
    $Ntdll = $Types['ntdll']
    $Ntdll::RtlGetCurrentPeb()
    $ntdllbase = $Kernel32::GetModuleHandle('ntdll')
    $Kernel32::GetProcAddress($ntdllbase, 'RtlGetCurrentPeb')

    .NOTES

    Inspired by Lee Holmes' Invoke-WindowsApi http://poshcode.org/2189

    When defining multiple function prototypes, it is ideal to provide
    Add-Win32Type with an array of function signatures. That way, they
    are all incorporated into the same in-memory module.
    #>

        [OutputType([Hashtable])]
        Param(
            [Parameter(Mandatory = $True, ValueFromPipelineByPropertyName = $True)]
            [String]
            $DllName,

            [Parameter(Mandatory = $True, ValueFromPipelineByPropertyName = $True)]
            [String]
            $FunctionName,

            [Parameter(ValueFromPipelineByPropertyName = $True)]
            [String]
            $EntryPoint,

            [Parameter(Mandatory = $True, ValueFromPipelineByPropertyName = $True)]
            [Type]
            $ReturnType,

            [Parameter(ValueFromPipelineByPropertyName = $True)]
            [Type[]]
            $ParameterTypes,

            [Parameter(ValueFromPipelineByPropertyName = $True)]
            [Runtime.InteropServices.CallingConvention]
            $NativeCallingConvention = [Runtime.InteropServices.CallingConvention]::StdCall,

            [Parameter(ValueFromPipelineByPropertyName = $True)]
            [Runtime.InteropServices.CharSet]
            $Charset = [Runtime.InteropServices.CharSet]::Auto,

            [Parameter(ValueFromPipelineByPropertyName = $True)]
            [Switch]
            $SetLastError,

            [Parameter(Mandatory = $True)]
            [ValidateScript({($_ -is [Reflection.Emit.ModuleBuilder]) -or ($_ -is [Reflection.Assembly])})]
            $Module,

            [ValidateNotNull()]
            [String]
            $Namespace = ''
        )

        BEGIN
        {
            $TypeHash = @{}
        }

        PROCESS
        {
            if ($Module -is [Reflection.Assembly])
            {
                if ($Namespace)
                {
                    $TypeHash[$DllName] = $Module.GetType("$Namespace.$DllName")
                }
                else
                {
                    $TypeHash[$DllName] = $Module.GetType($DllName)
                }
            }
            else
            {
                # Define one type for each DLL
                if (!$TypeHash.ContainsKey($DllName))
                {
                    if ($Namespace)
                    {
                        $TypeHash[$DllName] = $Module.DefineType("$Namespace.$DllName", 'Public,BeforeFieldInit')
                    }
                    else
                    {
                        $TypeHash[$DllName] = $Module.DefineType($DllName, 'Public,BeforeFieldInit')
                    }
                }

                $Method = $TypeHash[$DllName].DefineMethod(
                    $FunctionName,
                    'Public,Static,PinvokeImpl',
                    $ReturnType,
                    $ParameterTypes)

                # Make each ByRef parameter an Out parameter
                $i = 1
                foreach($Parameter in $ParameterTypes)
                {
                    if ($Parameter.IsByRef)
                    {
                        [void] $Method.DefineParameter($i, 'Out', $null)
                    }

                    $i++
                }

                $DllImport = [Runtime.InteropServices.DllImportAttribute]
                $SetLastErrorField = $DllImport.GetField('SetLastError')
                $CallingConventionField = $DllImport.GetField('CallingConvention')
                $CharsetField = $DllImport.GetField('CharSet')
                $EntryPointField = $DllImport.GetField('EntryPoint')
                if ($SetLastError) { $SLEValue = $True } else { $SLEValue = $False }

                if ($PSBoundParameters['EntryPoint']) { $ExportedFuncName = $EntryPoint } else { $ExportedFuncName = $FunctionName }

                # Equivalent to C# version of [DllImport(DllName)]
                $Constructor = [Runtime.InteropServices.DllImportAttribute].GetConstructor([String])
                $DllImportAttribute = New-Object Reflection.Emit.CustomAttributeBuilder($Constructor,
                    $DllName, [Reflection.PropertyInfo[]] @(), [Object[]] @(),
                    [Reflection.FieldInfo[]] @($SetLastErrorField,
                                               $CallingConventionField,
                                               $CharsetField,
                                               $EntryPointField),
                    [Object[]] @($SLEValue,
                                 ([Runtime.InteropServices.CallingConvention] $NativeCallingConvention),
                                 ([Runtime.InteropServices.CharSet] $Charset),
                                 $ExportedFuncName))

                $Method.SetCustomAttribute($DllImportAttribute)
            }
        }

        END
        {
            if ($Module -is [Reflection.Assembly])
            {
                return $TypeHash
            }

            $ReturnTypes = @{}

            foreach ($Key in $TypeHash.Keys)
            {
                $Type = $TypeHash[$Key].CreateType()
            
                $ReturnTypes[$Key] = $Type
            }

            return $ReturnTypes
        }
    }

    function psenum
    {
    <#
    .SYNOPSIS

    Creates an in-memory enumeration for use in your PowerShell session.

    Author: Matthew Graeber (@mattifestation)
    License: BSD 3-Clause
    Required Dependencies: None
    Optional Dependencies: None
 
    .DESCRIPTION

    The 'psenum' function facilitates the creation of enums entirely in
    memory using as close to a "C style" as PowerShell will allow.

    .PARAMETER Module

    The in-memory module that will host the enum. Use
    New-InMemoryModule to define an in-memory module.

    .PARAMETER FullName

    The fully-qualified name of the enum.

    .PARAMETER Type

    The type of each enum element.

    .PARAMETER EnumElements

    A hashtable of enum elements.

    .PARAMETER Bitfield

    Specifies that the enum should be treated as a bitfield.

    .EXAMPLE

    $Mod = New-InMemoryModule -ModuleName Win32

    $ImageSubsystem = psenum $Mod PE.IMAGE_SUBSYSTEM UInt16 @{
        UNKNOWN =                  0
        NATIVE =                   1 # Image doesn't require a subsystem.
        WINDOWS_GUI =              2 # Image runs in the Windows GUI subsystem.
        WINDOWS_CUI =              3 # Image runs in the Windows character subsystem.
        OS2_CUI =                  5 # Image runs in the OS/2 character subsystem.
        POSIX_CUI =                7 # Image runs in the Posix character subsystem.
        NATIVE_WINDOWS =           8 # Image is a native Win9x driver.
        WINDOWS_CE_GUI =           9 # Image runs in the Windows CE subsystem.
        EFI_APPLICATION =          10
        EFI_BOOT_SERVICE_DRIVER =  11
        EFI_RUNTIME_DRIVER =       12
        EFI_ROM =                  13
        XBOX =                     14
        WINDOWS_BOOT_APPLICATION = 16
    }

    .NOTES

    PowerShell purists may disagree with the naming of this function but
    again, this was developed in such a way so as to emulate a "C style"
    definition as closely as possible. Sorry, I'm not going to name it
    New-Enum. :P
    #>

        [OutputType([Type])]
        Param
        (
            [Parameter(Position = 0, Mandatory = $True)]
            [ValidateScript({($_ -is [Reflection.Emit.ModuleBuilder]) -or ($_ -is [Reflection.Assembly])})]
            $Module,

            [Parameter(Position = 1, Mandatory = $True)]
            [ValidateNotNullOrEmpty()]
            [String]
            $FullName,

            [Parameter(Position = 2, Mandatory = $True)]
            [Type]
            $Type,

            [Parameter(Position = 3, Mandatory = $True)]
            [ValidateNotNullOrEmpty()]
            [Hashtable]
            $EnumElements,

            [Switch]
            $Bitfield
        )

        if ($Module -is [Reflection.Assembly])
        {
            return ($Module.GetType($FullName))
        }

        $EnumType = $Type -as [Type]

        $EnumBuilder = $Module.DefineEnum($FullName, 'Public', $EnumType)

        if ($Bitfield)
        {
            $FlagsConstructor = [FlagsAttribute].GetConstructor(@())
            $FlagsCustomAttribute = New-Object Reflection.Emit.CustomAttributeBuilder($FlagsConstructor, @())
            $EnumBuilder.SetCustomAttribute($FlagsCustomAttribute)
        }

        foreach ($Key in $EnumElements.Keys)
        {
            # Apply the specified enum type to each element
            $null = $EnumBuilder.DefineLiteral($Key, $EnumElements[$Key] -as $EnumType)
        }

        $EnumBuilder.CreateType()
    }

    # A helper function used to reduce typing while defining struct
    # fields.
    function field
    {
        Param
        (
            [Parameter(Position = 0, Mandatory = $True)]
            [UInt16]
            $Position,
        
            [Parameter(Position = 1, Mandatory = $True)]
            [Type]
            $Type,
        
            [Parameter(Position = 2)]
            [UInt16]
            $Offset,
        
            [Object[]]
            $MarshalAs
        )

        @{
            Position = $Position
            Type = $Type -as [Type]
            Offset = $Offset
            MarshalAs = $MarshalAs
        }
    }

    function struct
    {
    <#
    .SYNOPSIS

    Creates an in-memory struct for use in your PowerShell session.

    Author: Matthew Graeber (@mattifestation)
    License: BSD 3-Clause
    Required Dependencies: None
    Optional Dependencies: field
 
    .DESCRIPTION

    The 'struct' function facilitates the creation of structs entirely in
    memory using as close to a "C style" as PowerShell will allow. Struct
    fields are specified using a hashtable where each field of the struct
    is comprosed of the order in which it should be defined, its .NET
    type, and optionally, its offset and special marshaling attributes.

    One of the features of 'struct' is that after your struct is defined,
    it will come with a built-in GetSize method as well as an explicit
    converter so that you can easily cast an IntPtr to the struct without
    relying upon calling SizeOf and/or PtrToStructure in the Marshal
    class.

    .PARAMETER Module

    The in-memory module that will host the struct. Use
    New-InMemoryModule to define an in-memory module.

    .PARAMETER FullName

    The fully-qualified name of the struct.

    .PARAMETER StructFields

    A hashtable of fields. Use the 'field' helper function to ease
    defining each field.

    .PARAMETER PackingSize

    Specifies the memory alignment of fields.

    .PARAMETER ExplicitLayout

    Indicates that an explicit offset for each field will be specified.

    .EXAMPLE

    $Mod = New-InMemoryModule -ModuleName Win32

    $ImageDosSignature = psenum $Mod PE.IMAGE_DOS_SIGNATURE UInt16 @{
        DOS_SIGNATURE =    0x5A4D
        OS2_SIGNATURE =    0x454E
        OS2_SIGNATURE_LE = 0x454C
        VXD_SIGNATURE =    0x454C
    }

    $ImageDosHeader = struct $Mod PE.IMAGE_DOS_HEADER @{
        e_magic =    field 0 $ImageDosSignature
        e_cblp =     field 1 UInt16
        e_cp =       field 2 UInt16
        e_crlc =     field 3 UInt16
        e_cparhdr =  field 4 UInt16
        e_minalloc = field 5 UInt16
        e_maxalloc = field 6 UInt16
        e_ss =       field 7 UInt16
        e_sp =       field 8 UInt16
        e_csum =     field 9 UInt16
        e_ip =       field 10 UInt16
        e_cs =       field 11 UInt16
        e_lfarlc =   field 12 UInt16
        e_ovno =     field 13 UInt16
        e_res =      field 14 UInt16[] -MarshalAs @('ByValArray', 4)
        e_oemid =    field 15 UInt16
        e_oeminfo =  field 16 UInt16
        e_res2 =     field 17 UInt16[] -MarshalAs @('ByValArray', 10)
        e_lfanew =   field 18 Int32
    }

    # Example of using an explicit layout in order to create a union.
    $TestUnion = struct $Mod TestUnion @{
        field1 = field 0 UInt32 0
        field2 = field 1 IntPtr 0
    } -ExplicitLayout

    .NOTES

    PowerShell purists may disagree with the naming of this function but
    again, this was developed in such a way so as to emulate a "C style"
    definition as closely as possible. Sorry, I'm not going to name it
    New-Struct. :P
    #>

        [OutputType([Type])]
        Param
        (
            [Parameter(Position = 1, Mandatory = $True)]
            [ValidateScript({($_ -is [Reflection.Emit.ModuleBuilder]) -or ($_ -is [Reflection.Assembly])})]
            $Module,

            [Parameter(Position = 2, Mandatory = $True)]
            [ValidateNotNullOrEmpty()]
            [String]
            $FullName,

            [Parameter(Position = 3, Mandatory = $True)]
            [ValidateNotNullOrEmpty()]
            [Hashtable]
            $StructFields,

            [Reflection.Emit.PackingSize]
            $PackingSize = [Reflection.Emit.PackingSize]::Unspecified,

            [Switch]
            $ExplicitLayout
        )

        if ($Module -is [Reflection.Assembly])
        {
            return ($Module.GetType($FullName))
        }

        [Reflection.TypeAttributes] $StructAttributes = 'AnsiClass,
            Class,
            Public,
            Sealed,
            BeforeFieldInit'

        if ($ExplicitLayout)
        {
            $StructAttributes = $StructAttributes -bor [Reflection.TypeAttributes]::ExplicitLayout
        }
        else
        {
            $StructAttributes = $StructAttributes -bor [Reflection.TypeAttributes]::SequentialLayout
        }

        $StructBuilder = $Module.DefineType($FullName, $StructAttributes, [ValueType], $PackingSize)
        $ConstructorInfo = [Runtime.InteropServices.MarshalAsAttribute].GetConstructors()[0]
        $SizeConst = @([Runtime.InteropServices.MarshalAsAttribute].GetField('SizeConst'))

        $Fields = New-Object Hashtable[]($StructFields.Count)

        # Sort each field according to the orders specified
        # Unfortunately, PSv2 doesn't have the luxury of the
        # hashtable [Ordered] accelerator.
        foreach ($Field in $StructFields.Keys)
        {
            $Index = $StructFields[$Field]['Position']
            $Fields[$Index] = @{FieldName = $Field; Properties = $StructFields[$Field]}
        }

        foreach ($Field in $Fields)
        {
            $FieldName = $Field['FieldName']
            $FieldProp = $Field['Properties']

            $Offset = $FieldProp['Offset']
            $Type = $FieldProp['Type']
            $MarshalAs = $FieldProp['MarshalAs']

            $NewField = $StructBuilder.DefineField($FieldName, $Type, 'Public')

            if ($MarshalAs)
            {
                $UnmanagedType = $MarshalAs[0] -as ([Runtime.InteropServices.UnmanagedType])
                if ($MarshalAs[1])
                {
                    $Size = $MarshalAs[1]
                    $AttribBuilder = New-Object Reflection.Emit.CustomAttributeBuilder($ConstructorInfo,
                        $UnmanagedType, $SizeConst, @($Size))
                }
                else
                {
                    $AttribBuilder = New-Object Reflection.Emit.CustomAttributeBuilder($ConstructorInfo, [Object[]] @($UnmanagedType))
                }
            
                $NewField.SetCustomAttribute($AttribBuilder)
            }

            if ($ExplicitLayout) { $NewField.SetOffset($Offset) }
        }

        # Make the struct aware of its own size.
        # No more having to call [Runtime.InteropServices.Marshal]::SizeOf!
        $SizeMethod = $StructBuilder.DefineMethod('GetSize',
            'Public, Static',
            [Int],
            [Type[]] @())
        $ILGenerator = $SizeMethod.GetILGenerator()
        # Thanks for the help, Jason Shirk!
        $ILGenerator.Emit([Reflection.Emit.OpCodes]::Ldtoken, $StructBuilder)
        $ILGenerator.Emit([Reflection.Emit.OpCodes]::Call,
            [Type].GetMethod('GetTypeFromHandle'))
        $ILGenerator.Emit([Reflection.Emit.OpCodes]::Call,
            [Runtime.InteropServices.Marshal].GetMethod('SizeOf', [Type[]] @([Type])))
        $ILGenerator.Emit([Reflection.Emit.OpCodes]::Ret)

        # Allow for explicit casting from an IntPtr
        # No more having to call [Runtime.InteropServices.Marshal]::PtrToStructure!
        $ImplicitConverter = $StructBuilder.DefineMethod('op_Implicit',
            'PrivateScope, Public, Static, HideBySig, SpecialName',
            $StructBuilder,
            [Type[]] @([IntPtr]))
        $ILGenerator2 = $ImplicitConverter.GetILGenerator()
        $ILGenerator2.Emit([Reflection.Emit.OpCodes]::Nop)
        $ILGenerator2.Emit([Reflection.Emit.OpCodes]::Ldarg_0)
        $ILGenerator2.Emit([Reflection.Emit.OpCodes]::Ldtoken, $StructBuilder)
        $ILGenerator2.Emit([Reflection.Emit.OpCodes]::Call,
            [Type].GetMethod('GetTypeFromHandle'))
        $ILGenerator2.Emit([Reflection.Emit.OpCodes]::Call,
            [Runtime.InteropServices.Marshal].GetMethod('PtrToStructure', [Type[]] @([IntPtr], [Type])))
        $ILGenerator2.Emit([Reflection.Emit.OpCodes]::Unbox_Any, $StructBuilder)
        $ILGenerator2.Emit([Reflection.Emit.OpCodes]::Ret)

        $StructBuilder.CreateType()
    }
    #endregion PSReflect

    $Module = New-InMemoryModule -ModuleName GetKerberosTicket

    #region Enums
    $KERB_PROTOCOL_MESSAGE_TYPE = psenum $Module KERB_PROTOCOL_MESSAGE_TYPE UInt32 @{ 
        KerbDebugRequestMessage                  = 0
        KerbQueryTicketCacheMessage              = 1
        KerbChangeMachinePasswordMessage         = 2
        KerbVerifyPacMessage                     = 3
        KerbRetrieveTicketMessage                = 4
        KerbUpdateAddressesMessage               = 5
        KerbPurgeTicketCacheMessage              = 6
        KerbChangePasswordMessage                = 7
        KerbRetrieveEncodedTicketMessage         = 8
        KerbDecryptDataMessage                   = 9
        KerbAddBindingCacheEntryMessage          = 10
        KerbSetPasswordMessage                   = 11
        KerbSetPasswordExMessage                 = 12
        KerbVerifyCredentialsMessage             = 13
        KerbQueryTicketCacheExMessage            = 14
        KerbPurgeTicketCacheExMessage            = 15
        KerbRefreshSmartcardCredentialsMessage   = 16
        KerbAddExtraCredentialsMessage           = 17
        KerbQuerySupplementalCredentialsMessage  = 18
        KerbTransferCredentialsMessage           = 19
        KerbQueryTicketCacheEx2Message           = 20
        KerbSubmitTicketMessage                  = 21
        KerbAddExtraCredentialsExMessage         = 22
        KerbQueryKdcProxyCacheMessage            = 23
        KerbPurgeKdcProxyCacheMessage            = 24
        KerbQueryTicketCacheEx3Message           = 25
        KerbCleanupMachinePkinitCredsMessage     = 26
        KerbAddBindingCacheEntryExMessage        = 27
        KerbQueryBindingCacheMessage             = 28
        KerbPurgeBindingCacheMessage             = 29
        KerbQueryDomainExtendedPoliciesMessage   = 30
        KerbQueryS4U2ProxyCacheMessage           = 31
    }

    $KERB_CACHE_OPTIONS = psenum $Module KERB_CACHE_OPTIONS UInt64 @{
        KERB_RETRIEVE_TICKET_DONT_USE_CACHE = 0x1
        KERB_RETRIEVE_TICKET_USE_CACHE_ONLY = 0x2
        KERB_RETRIEVE_TICKET_USE_CREDHANDLE = 0x4
        KERB_RETRIEVE_TICKET_AS_KERB_CRED   = 0x8
        KERB_RETRIEVE_TICKET_WITH_SEC_CRED  = 0x10 
        KERB_RETRIEVE_TICKET_CACHE_TICKET   = 0x20
        KERB_RETRIEVE_TICKET_MAX_LIFETIME   = 0x40
    } -Bitfield

    $KERB_ENCRYPTION_TYPE = psenum $Module KERB_ENCRYPTION_TYPE UInt32 @{
          reserved0                         = 0
          des_cbc_crc                       = 1
          des_cbc_md4                       = 2
          des_cbc_md5                       = 3
          reserved1                         = 4
          des3_cbc_md5                      = 5
          reserved2                         = 6
          des3_cbc_sha1                     = 7
          dsaWithSHA1_CmsOID                = 9
          md5WithRSAEncryption_CmsOID       = 10
          sha1WithRSAEncryption_CmsOID      = 11
          rc2CBC_EnvOID                     = 12
          rsaEncryption_EnvOID              = 13
          rsaES_OAEP_ENV_OID                = 14
          des_ede3_cbc_Env_OID              = 15
          des3_cbc_sha1_kd                  = 16
          aes128_cts_hmac_sha1_96           = 17
          aes256_cts_hmac_sha1_96           = 18
          aes128_cts_hmac_sha256_128        = 19
          aes256_cts_hmac_sha384_192        = 20
          rc4_hmac                          = 23
          rc4_hmac_exp                      = 24
          camellia128_cts_cmac              = 25
          camellia256_cts_cmac              = 26
          subkey_keymaterial                = 65
    }

    $KERB_TICKET_FLAGS = psenum $Module KERB_TICKET_FLAGS UInt32 @{
        reserved          = 2147483648
        forwardable       = 0x40000000
        forwarded         = 0x20000000
        proxiable         = 0x10000000
        proxy             = 0x08000000
        may_postdate      = 0x04000000
        postdated         = 0x02000000
        invalid           = 0x01000000
        renewable         = 0x00800000
        initial           = 0x00400000
        pre_authent       = 0x00200000
        hw_authent        = 0x00100000
        ok_as_delegate    = 0x00040000
        name_canonicalize = 0x00010000
        cname_in_pa_data  = 0x00040000
        enc_pa_rep        = 0x00010000
        reserved1         = 0x00000001
    } -Bitfield

    $SECURITY_LOGON_TYPE = psenum $Module SECURITY_LOGON_TYPE UInt32 @{
        Interactive = 2
        Network     = 3
        Batch       = 4
        Service     = 5
        Proxy       = 6
        Unlock      = 7
        NetworkCleartext = 8
        NewCredentials = 9
        RemoteInteractive = 10
        CachedInteractive = 11
        CachedRemoteInteractive = 12
        CachedUnlock = 13
    }

    $SECURITY_IMPERSONATION_LEVEL = psenum $Module SECURITY_IMPERSONATION_LEVEL UInt32 @{
        SecurityAnonymous = 0
        SecurityIdentification = 1
        SecurityImpersonation = 2
        SecurityDelegation = 3
    }

    $TOKEN_ACCESS = psenum $Module TOKEN_ACCESS UInt32 @{
        TOKEN_DUPLICATE          = 0x00000002
        TOKEN_IMPERSONATE        = 0x00000004
        TOKEN_QUERY              = 0x00000008
        TOKEN_QUERY_SOURCE       = 0x00000010
        TOKEN_ADJUST_PRIVILEGES  = 0x00000020
        TOKEN_ADJUST_GROUPS      = 0x00000040
        TOKEN_ADJUST_DEFAULT     = 0x00000080
        TOKEN_ADJUST_SESSIONID   = 0x00000100
        DELETE                   = 0x00010000
        READ_CONTROL             = 0x00020000
        WRITE_DAC                = 0x00040000
        WRITE_OWNER              = 0x00080000
        SYNCHRONIZE              = 0x00100000
        STANDARD_RIGHTS_REQUIRED = 0x000F0000
        TOKEN_ALL_ACCESS         = 0x001f01ff
    } -Bitfield
    #endregion Enums

    #region Structs
    $LSA_STRING = struct $Module LSA_STRING @{
        Length = field 0 UInt16
        MaximumLength = field 1 UInt16
        Buffer = field 2 IntPtr
    }

    $LSA_UNICODE_STRING = struct $Module LSA_UNICODE_STRING @{
        Length = field 0 UInt16
        MaximumLength = field 1 UInt16
        Buffer = field 2 IntPtr
    }

    $LUID = struct $Module LUID @{
        LowPart  = field 0 UInt32
        HighPart = field 1 UInt32
    }

    $LUID_AND_ATTRIBUTES = struct $Module LUID_AND_ATTRIBUTES @{
        Luid       = field 0 $LUID
        Attributes = field 1 UInt32
    }

    $SecHandle = struct $Module SecHandle @{
        dwLower = field 0 IntPtr       
        dwUpper = field 1 IntPtr
    }

    $KERB_CRYPTO_KEY = struct $Module KERB_CRYPTO_KEY @{
        KeyType = field 0 Int32
        Length = field 1 Int32
        Value = field 2 IntPtr
    }

    $KERB_EXTERNAL_NAME = struct $Module KERB_EXTERNAL_NAME @{
        NameType = field 0 Int16
        NameCount = field 1 UInt16
        Names = field 2 $LSA_UNICODE_STRING
    }

    $KERB_EXTERNAL_TICKET = struct $Module KERB_EXTERNAL_TICKET @{
        ServiceName = field 0 IntPtr
        TargetName = field 1 IntPtr
        ClientName = field 2 IntPtr
        DomainName = field 3 $LSA_UNICODE_STRING
        TargetDomainName = field 4 $LSA_UNICODE_STRING
        AltTargetDomainName = field 5 $LSA_UNICODE_STRING
        SessionKey = field 6 $KERB_CRYPTO_KEY
        TicketFlags = field 7 UInt32
        Flags = field 8 UInt32
        KeyExpirationTime = field 9 Int64
        StartTime = field 10 Int64
        EndTime = field 11 Int64
        RenewUntil = field 12 Int64
        TimeSkew = field 13 Int64
        EncodedTicketSize = field 14 Int32
        EncodedTicket = field 15 IntPtr
    }

    $KERB_TICKET_CACHE_INFO = struct $Module KERB_TICKET_CACHE_INFO @{
        ServerName = field 0 $LSA_UNICODE_STRING
        RealmName = field 1 $LSA_UNICODE_STRING
        StartTime = field 2 Int64
        EndTime = field 3 Int64
        RenewTime = field 4 Int64
        EncryptionType = field 5 Int32
        TicketFlags = field 6 UInt32
    }

    $KERB_QUERY_TKT_CACHE_REQUEST = struct $Module KERB_QUERY_TKT_CACHE_REQUEST @{
        MessageType = field 0 $KERB_PROTOCOL_MESSAGE_TYPE
        LogonId = field 1 $LUID
    }

    $KERB_QUERY_TKT_CACHE_RESPONSE = struct $Module KERB_QUERY_TKT_CACHE_RESPONSE @{
        MessageType = field 0 $KERB_PROTOCOL_MESSAGE_TYPE
        CountOfTickets = field 1 UInt32
        Tickets = field 2 $KERB_TICKET_CACHE_INFO.MakeArrayType() -MarshalAs @('ByValArray', 1)
    }

    $KERB_RETRIEVE_TKT_REQUEST = struct $Module KERB_RETRIEVE_TKT_REQUEST @{
        MessageType = field 0 $KERB_PROTOCOL_MESSAGE_TYPE
        LogonId = field 1 $LUID
        TargetName = field 2 $LSA_UNICODE_STRING
        TicketFlags = field 3 UInt64
        CacheOptions = field 4 $KERB_CACHE_OPTIONS
        EncryptionType = field 5 Int64
        CredentialsHandle = field 6 $SecHandle
    }

    $KERB_RETRIEVE_TKT_RESPONSE = struct $Module KERB_RETRIEVE_TKT_RESPONSE @{
        Ticket = field 0 $KERB_EXTERNAL_TICKET
    }

    $LSA_LAST_INTER_LOGON_INFO = struct $Module LSA_LAST_INTER_LOGON_INFO @{
        LastSuccessfulLogon = field 0 Int64
        LastFailedLogon = field 1 Int64
        FailedAttemptCountSinceLastSuccessfulLogon = field 2 UInt64
    }

    $SECURITY_LOGON_SESSION_DATA = struct $Module SECURITY_LOGON_SESSION_DATA @{
        Size = field 0 UInt32
        LogonId = field 1 $LUID
        Username = field 2 $LSA_UNICODE_STRING
        LogonDomain = field 3 $LSA_UNICODE_STRING
        AuthenticationPackage = field 4 $LSA_UNICODE_STRING
        LogonType = field 5 UInt32
        Session = field 6 UInt32
        PSiD = field 7 IntPtr
        LogonTime = field 8 UInt64
        LogonServer = field 9 $LSA_UNICODE_STRING
        DnsDomainName = field 10 $LSA_UNICODE_STRING
        Upn = field 11 $LSA_UNICODE_STRING
        UserFlags = field 12 UInt64
        LastLogonInfo = field 13 $LSA_LAST_INTER_LOGON_INFO
        LogonScript = field 14 $LSA_UNICODE_STRING
        ProfilePath = field 15 $LSA_UNICODE_STRING
        HomeDirectory = field 16 $LSA_UNICODE_STRING
        HomeDirectoryDrive = field 17 $LSA_UNICODE_STRING
        LogoffTime = field 18 Int64
        KickOffTime = field 19 Int64
        PasswordLastSet = field 20 Int64
        PasswordCanChange = field 21 Int64
        PasswordMustChange = field 22 Int64
    }

    $SID_AND_ATTRIBUTES = struct $Module SID_AND_ATTRIBUTES @{
        Sid        = field 0 IntPtr
        Attributes = field 1 UInt32
    }
    #endregion Structs

    #region Function Definitions
    $FunctionDefinitions = @(
        (func kernel32 CloseHandle ([bool]) @(
            [IntPtr]                                  #_In_ HANDLE hObject
        ) -EntryPoint CloseHandle -SetLastError),
    
        (func advapi32 DuplicateToken ([bool]) @(
            [IntPtr],                                 #_In_  HANDLE                       ExistingTokenHandle,
            [UInt32],                                 #_In_  SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,
            [IntPtr].MakeByRefType()                  #_Out_ PHANDLE                      DuplicateTokenHandle
        ) -EntryPoint DuplicateToken -SetLastError),
    
        (func advapi32 ImpersonateLoggedOnUser ([bool]) @(
            [IntPtr]                                  #_In_ HANDLE hToken
        ) -EntryPoint ImpersonateLoggedOnUser -SetLastError),
    
        (func secur32 LsaCallAuthenticationPackage_KERB_QUERY_TKT_CACHE ([UInt32]) @(
            [IntPtr],                                      #_In_  HANDLE    LsaHandle
            [UInt64],                                      #_In_  ULONG     AuthenticationPackage
            $KERB_QUERY_TKT_CACHE_REQUEST.MakeByRefType(), #_In_  PVOID     ProtocolSubmitBuffer
            [UInt64],                                      #_In_  ULONG     SubmitBufferLength
            [IntPtr].MakeByRefType(),#_Out_ PVOID     *ProtocolReturnBuffer
            [UInt64].MakeByRefType(),                      #_Out_ PULONG    *ReturnBufferLength
            [UInt32].MakeByRefType()                       #_Out_ PNTSTATUS ProtocolStatus
        ) -EntryPoint LsaCallAuthenticationPackage),
    
        (func secur32 LsaCallAuthenticationPackage_KERB_RETRIEVE_TKT ([UInt32]) @(
            [IntPtr],                                   #_In_  HANDLE    LsaHandle
            [UInt64],                                   #_In_  ULONG     AuthenticationPackage
            $KERB_RETRIEVE_TKT_REQUEST.MakeByRefType(), #_In_  PVOID     ProtocolSubmitBuffer
            [UInt64],                                   #_In_  ULONG     SubmitBufferLength
            [IntPtr].MakeByRefType(),#_Out_ PVOID     *ProtocolReturnBuffer
            [UInt64].MakeByRefType(),                   #_Out_ PULONG    *ReturnBufferLength
            [UInt32].MakeByRefType()                    #_Out_ PNTSTATUS ProtocolStatus
        ) -EntryPoint LsaCallAuthenticationPackage),
    
        (func secur32 LsaConnectUntrusted ([UInt32]) @(
            [IntPtr].MakeByRefType()                #_Out_ PHANDLE LsaHandle
        ) -EntryPoint LsaConnectUntrusted),
    
        (func secur32 LsaDeregisterLogonProcess ([UInt32]) @(
            [IntPtr]                                #_In_ HANDLE LsaHandle
        ) -EntryPoint LsaDeregisterLogonProcess),
    
        (func secur32 LsaEnumerateLogonSessions ([UInt32]) @(
            [UInt64].MakeByRefType(),               #_Out_ PULONG LogonSessionCount,
            [IntPtr].MakeByRefType()                #_Out_ PLUID  *LogonSessionList
        ) -EntryPoint LsaEnumerateLogonSessions),
    
        (func secur32 LsaFreeReturnBuffer ([UInt32]) @(
            [IntPtr].MakeByRefType()                #_In_ PVOID Buffer
        ) -EntryPoint LsaFreeReturnBuffer),
    
        (func secur32 LsaGetLogonSessionData ([UInt32]) @(
            [IntPtr],                                    #_In_  PLUID                        LogonId,
            [IntPtr].MakeByRefType()                     #_Out_ PSECURITY_LOGON_SESSION_DATA *ppLogonSessionData
        ) -EntryPoint LsaGetLogonSessionData),
    
        (func secur32 LsaLookupAuthenticationPackage ([UInt32]) @(
            [IntPtr],                               #_In_  HANDLE      LsaHandle,
            $LSA_STRING.MakeByRefType()             #_In_  PLSA_STRING PackageName,
            [UInt64].MakeByRefType()                #_Out_ PULONG      AuthenticationPackage
        ) -EntryPoint LsaLookupAuthenticationPackage),
    
        (func advapi32 LsaNtStatusToWinError ([UInt64]) @(
            [UInt32]                                #_In_ NTSTATUS Status
        ) -EntryPoint LsaNtStatusToWinError),
    
        (func secur32 LsaRegisterLogonProcess ([UInt32]) @(
            $LSA_STRING.MakeByRefType()             #_In_  PLSA_STRING           LogonProcessName,
            [IntPtr].MakeByRefType()                #_Out_ PHANDLE               LsaHandle,
            [UInt64].MakeByRefType()                #_Out_ PLSA_OPERATIONAL_MODE SecurityMode
        ) -EntryPoint LsaRegisterLogonProcess),
    
        (func advapi32 OpenProcessToken ([bool]) @(
            [IntPtr],                                   #_In_  HANDLE  ProcessHandle
            [UInt32],                                   #_In_  DWORD   DesiredAccess
            [IntPtr].MakeByRefType()                    #_Out_ PHANDLE TokenHandle
        ) -EntryPoint OpenProcessToken -SetLastError),
    
        (func advapi32 RevertToSelf ([bool]) @() -EntryPoint RevertToSelf -SetLastError)
    )

    $Types = $FunctionDefinitions | Add-Win32Type -Module $Module -Namespace 'Kerberos'
    
    $Advapi32 = $Types['advapi32']
    $Kernel32 = $Types['kernel32']
    $Secur32 = $Types['secur32']
    #endregion Function Definitions

    #region Win32 function abstractions
    function CloseHandle
    {
        <#
        .SYNOPSIS

        Closes an open object handle.

        .DESCRIPTION

        The CloseHandle function closes handles to the following objects:
        - Access token
        - Communications device
        - Console input
        - Console screen buffer
        - Event
        - File
        - File mapping
        - I/O completion port
        - Job
        - Mailslot
        - Memory resource notification
        - Mutex
        - Named pipe
        - Pipe
        - Process
        - Semaphore
        - Thread
        - Transaction
        - Waitable timer
    
        The documentation for the functions that create these objects indicates that CloseHandle should be used when you are finished with the object, and what happens to pending operations on the object after the handle is closed. In general, CloseHandle invalidates the specified object handle, decrements the object's handle count, and performs object retention checks. After the last handle to an object is closed, the object is removed from the system. 

        .PARAMETER Handle

        A valid handle to an open object.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect
        Optional Dependencies: None
    
        (func kernel32 CloseHandle ([bool]) @(
            [IntPtr] #_In_ HANDLE hObject
        ) -EntryPoint CloseHandle -SetLastError)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/ms724211(v=vs.85).aspx

        .EXAMPLE
        #>

        param
        (
            [Parameter(Mandatory = $true)]
            [IntPtr]
            $Handle    
        )
    
        $SUCCESS = $Kernel32::CloseHandle($Handle); $LastError = [Runtime.InteropServices.Marshal]::GetLastWin32Error()

        if(-not $SUCCESS) 
        {
            Write-Debug "CloseHandle Error: $(([ComponentModel.Win32Exception] $LastError).Message)"
        }
    }

    function DuplicateToken
    {
        <#
        .SYNOPSIS

        The DuplicateToken function creates a new access token that duplicates one already in existence.

        .DESCRIPTION

        The DuplicateToken function creates an impersonation token, which you can use in functions such as SetThreadToken and ImpersonateLoggedOnUser. The token created by DuplicateToken cannot be used in the CreateProcessAsUser function, which requires a primary token. To create a token that you can pass to CreateProcessAsUser, use the DuplicateTokenEx function.

        .PARAMETER TokenHandle

        A handle to an access token opened with TOKEN_DUPLICATE access.

        .PARAMETER ImpersonationLevel

        Specifies a SECURITY_IMPERSONATION_LEVEL enumerated type that supplies the impersonation level of the new token. The Default is SecurityImpersonation.

        .NOTES
    
        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect, SECURITY_IMPERSONATION_LEVEL (Enumeration)
        Optional Dependencies: None

        (func advapi32 DuplicateToken ([bool]) @(
            [IntPtr]                 #_In_  HANDLE                       ExistingTokenHandle,
            [UInt32]                 #_In_  SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,
            [IntPtr].MakeByRefType() #_Out_ PHANDLE                      DuplicateTokenHandle
        ) -EntryPoint DuplicateToken -SetLastError)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa446616(v=vs.85).aspx

        .EXAMPLE

        #>

        [OutputType([IntPtr])]
        [CmdletBinding()]
        param
        (
            [Parameter(Mandatory = $true)]
            [IntPtr]
            $TokenHandle,

            [Parameter()]
            [ValidateSet('None','SecurityAnonymous','SecurityIdentification','SecurityImpersonation','SecurityDelegation')]
            [string]
            $ImpersonationLevel = 'SecurityImpersonation'
        )

        $DuplicateTokenHandle = [IntPtr]::Zero

        $success = $Advapi32::DuplicateToken($TokenHandle, $SECURITY_IMPERSONATION_LEVEL::$ImpersonationLevel, [ref]$DuplicateTokenHandle); $LastError = [Runtime.InteropServices.Marshal]::GetLastWin32Error()
    
        if(-not $success)
        {
            Write-Debug "DuplicateToken Error: $(([ComponentModel.Win32Exception] $LastError).Message)"
        }

        Write-Output $DuplicateTokenHandle
    }

    function ImpersonateLoggedOnUser
    {
        <#
        .SYNOPSIS

        The ImpersonateLoggedOnUser function lets the calling thread impersonate the security context of a logged-on user. The user is represented by a token handle.

        .DESCRIPTION

        The impersonation lasts until the thread exits or until it calls RevertToSelf.
    
        The calling thread does not need to have any particular privileges to call ImpersonateLoggedOnUser.
    
        If the call to ImpersonateLoggedOnUser fails, the client connection is not impersonated and the client request is made in the security context of the process. If the process is running as a highly privileged account, such as LocalSystem, or as a member of an administrative group, the user may be able to perform actions they would otherwise be disallowed. Therefore, it is important to always check the return value of the call, and if it fails, raise an error; do not continue execution of the client request.
    
        All impersonate functions, including ImpersonateLoggedOnUser allow the requested impersonation if one of the following is true:
        - The requested impersonation level of the token is less than SecurityImpersonation, such as SecurityIdentification or SecurityAnonymous.
        - The caller has the SeImpersonatePrivilege privilege.
        - A process (or another process in the caller's logon session) created the token using explicit credentials through LogonUser or LsaLogonUser function.
        - The authenticated identity is same as the caller.
    
        Windows XP with SP1 and earlier:  The SeImpersonatePrivilege privilege is not supported.

        .PARAMETER TokenHandle

        A handle to a primary or impersonation access token that represents a logged-on user. This can be a token handle returned by a call to LogonUser, CreateRestrictedToken, DuplicateToken, DuplicateTokenEx, OpenProcessToken, or OpenThreadToken functions. If hToken is a handle to a primary token, the token must have TOKEN_QUERY and TOKEN_DUPLICATE access. If hToken is a handle to an impersonation token, the token must have TOKEN_QUERY and TOKEN_IMPERSONATE access.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect
        Optional Dependencies: None

        (func advapi32 ImpersonateLoggedOnUser ([bool]) @(
            [IntPtr] #_In_ HANDLE hToken
        ) -EntryPoint ImpersonateLoggedOnUser -SetLastError)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa378612(v=vs.85).aspx

        .EXAMPLE

        #>

        param
        (
            [Parameter(Mandatory = $true)]
            [IntPtr]
            $TokenHandle
        )

        $SUCCESS = $Advapi32::ImpersonateLoggedOnUser($TokenHandle); $LastError = [Runtime.InteropServices.Marshal]::GetLastWin32Error()
    
        if(-not $SUCCESS)
        {
            throw "ImpersonateLoggedOnUser Error: $(([ComponentModel.Win32Exception] $LastError).Message)"
        }
    }

    function LsaCallAuthenticationPackage
    {
        <#
        .SYNOPSIS

        The LsaCallAuthenticationPackage function is used by a logon application to communicate with an authentication package.
    
        This function is typically used to access services provided by the authentication package.

        .DESCRIPTION

        Logon applications can call LsaCallAuthenticationPackage to communicate with an authentication package. There are several reasons why an application may do this:
    
        - To implement multiple-message authentication protocols, such as the NTLM Challenge-Response protocol.
        - To pass state change information to the authentication package. For example, the NTLM might notify the MSV1_0 package that a previously unreachable domain controller is now reachable. The authentication package would then re-logon any users logged on to that domain controller.
    
        Typically, this function is used to exchange information with a custom authentication package. This function is not needed by an application that is using one of the authentication packages supplied with Windows, such as MSV1_0 or Kerberos.
    
        You must call LsaCallAuthenticationPackage to clean up PKINIT device credentials for LOCAL_SYSTEM and NETWORK_SERVICE. When there is no PKINIT device credential, a successful call does no operation. When there is a PKINIT device credential, a successful call cleans up the PKINIT device credential so that only the password credential remains.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: None
        Optional Dependencies: None

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa378261(v=vs.85).aspx

        .EXAMPLE

        #>

        param
        (
            [Parameter(Mandatory = $true)]
            [IntPtr]
            $LsaHandle,

            [Parameter()]
            [ValidateSet('MICROSOFT_KERBEROS_NAME_A')]
            [string]
            $AuthenticationPackageName = 'MICROSOFT_KERBEROS_NAME_A',

            [Parameter(Mandatory = $true)]
            [UInt32]
            $LogonId
        )

        <#
        (func secur32 LsaCallAuthenticationPackage ([UInt32]) @(
            [IntPtr],                                  #_In_  HANDLE    LsaHandle
            [UInt64],                                  #_In_  ULONG     AuthenticationPackage
            $KERB_RETRIEVE_TKT_REQUEST.MakeByRefType(),#_In_  PVOID     ProtocolSubmitBuffer
            [UInt64],                                  #_In_  ULONG     SubmitBufferLength
            [IntPtr],                                  #_Out_ PVOID     *ProtocolReturnBuffer
            [UInt64].MakeByRefType(),                  #_Out_ PULONG    *ReturnBufferLength
            [UInt32].MakeByRefType()                   #_Out_ PNTSTATUS ProtocolStatus
        ))
        #>

        $AuthenticationPackage = LsaLookupAuthenticationPackage -LsaHandle $LsaHandle -PackageName $AuthenticationPackageName

        switch($AuthenticationPackageName)
        {
            MICROSOFT_KERBEROS_NAME_A
            {
                $LogonIdLuid = [Activator]::CreateInstance($LUID)
                $LogonIdLuid.LowPart = $LogonId
                $LogonIdLuid.HighPart = 0


                # Check Ticket Granting Ticket
                <#
                $KERB_RETRIEVE_TKT_REQUEST = struct $Mod Kerberos.KERB_RETRIEVE_TKT_REQUEST @{
                    MessageType = field 0 $KERB_PROTOCOL_MESSAGE_TYPE
                    LogonId = field 1 $LUID
                    TargetName = field 2 $LSA_UNICODE_STRING
                    TicketFlags = field 3 UInt64
                    CacheOptions = field 4 $KERB_CACHE_OPTIONS
                    EncryptionType = field 5 Int64
                    CredentialsHandle = field 6 IntPtr
                }
                #>

                $ProtocolSubmitBuffer = [Activator]::CreateInstance($KERB_RETRIEVE_TKT_REQUEST)
                $ProtocolSubmitBuffer.MessageType = $KERB_PROTOCOL_MESSAGE_TYPE::KerbRetrieveTicketMessage
                $ProtocolSubmitBuffer.LogonId = $LogonIdLuid

                $ProtocolReturnBuffer = [IntPtr]::Zero
                $ReturnBufferLength = [UInt64]0
                $ProtocolStatus = [UInt32]0

                $SUCCESS = $Secur32::LsaCallAuthenticationPackage_KERB_RETRIEVE_TKT($LsaHandle, $AuthenticationPackage, [ref]$ProtocolSubmitBuffer, $KERB_RETRIEVE_TKT_REQUEST::GetSize(), [ref]$ProtocolReturnBuffer, [ref]$ReturnBufferLength, [ref]$ProtocolStatus)

                if($SUCCESS -eq 0)
                {
                    if($ProtocolStatus -eq 0)
                    {
                        $data = $ProtocolReturnBuffer -as $KERB_RETRIEVE_TKT_RESPONSE
                    
                        #LsaFreeReturnBuffer -Buffer $ProtocolReturnBuffer

                        $ServiceName_STRING = $data.Ticket.ServiceName -as $KERB_EXTERNAL_NAME
                        $ServiceName = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($ServiceName_STRING.Names.Buffer, $ServiceName_STRING.Names.Length / 2)
                        #$TargetName_STRING = $data.Ticket.TargetName -as $KERB_EXTERNAL_NAME
                        #$TargetName = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($TargetName_STRING.Names.Buffer, $TargetName_STRING.Names.Length / 2)
                        $ClientName_STRING = $data.Ticket.ClientName -as $KERB_EXTERNAL_NAME
                        $ClientName = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($ClientName_STRING.Names.Buffer, $ClientName_STRING.Names.Length / 2)
                        $DomainName = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($data.Ticket.DomainName.Buffer, $data.Ticket.DomainName.Length / 2)

                        $TargetDomainName = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($data.Ticket.TargetDomainName.Buffer, $data.Ticket.TargetDomainName.Length / 2)
                        $AltTargetDomainName = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($data.Ticket.AltTargetDomainName.Buffer, $data.Ticket.AltTargetDomainName.Length / 2)
                        
                        # Session Key
                        $SessionKeyType = [string]($data.Ticket.SessionKey.KeyType -as $KERB_ENCRYPTION_TYPE)
                        $SessionKey = New-Object -TypeName byte[]($data.Ticket.SessionKey.Length)
                        [System.Runtime.InteropServices.Marshal]::Copy($data.Ticket.SessionKey.Value, $SessionKey, 0, $data.Ticket.SessionKey.Length)

                        # EncodedTicket Property
                        $EncodedTicket = New-Object -TypeName byte[]($data.Ticket.EncodedTicketSize)
                        [System.Runtime.InteropServices.Marshal]::Copy($data.Ticket.EncodedTicket, $EncodedTicket, 0, $data.Ticket.EncodedTicketSize)

                        $obj = New-Object -TypeName psobject
                    
                        $obj | Add-Member -MemberType NoteProperty -Name ServiceName -Value $ServiceName
                        #$obj | Add-Member -MemberType NoteProperty -Name TargetName -Value $TargetName
                        $obj | Add-Member -MemberType NoteProperty -Name ClientName -Value $ClientName
                        $obj | Add-Member -MemberType NoteProperty -Name DomainName -Value $DomainName
                        $obj | Add-Member -MemberType NoteProperty -Name TargetDomainName -Value $TargetDomainName
                        $obj | Add-Member -MemberType NoteProperty -Name AltTargetDomainName -Value $AltTargetDomainName
                        $obj | Add-Member -MemberType NoteProperty -Name SessionKeyType -Value $SessionKeyType
                        $obj | Add-Member -MemberType NoteProperty -Name SessionKey -Value $SessionKey
                        $obj | Add-Member -MemberType NoteProperty -Name TicketFlags -Value ($data.Ticket.TicketFlags -as $KERB_TICKET_FLAGS).ToString()
                        $obj | Add-Member -MemberType NoteProperty -Name KeyExpirationTime -Value ([datetime]::FromFileTime($data.Ticket.KeyExpirationTime))
                        $obj | Add-Member -MemberType NoteProperty -Name StartTime -Value ([datetime]::FromFileTime($data.Ticket.StartTime))
                        $obj | Add-Member -MemberType NoteProperty -Name EndTime -Value ([datetime]::FromFileTime($data.Ticket.EndTime))
                        $obj | Add-Member -MemberType NoteProperty -Name RenewUntil -Value ([datetime]::FromFileTime($data.Ticket.RenewUntil))
                        $obj | Add-Member -MemberType NoteProperty -Name TimeSkew -Value $data.Ticket.TimeSkew
                        $obj | Add-Member -MemberType NoteProperty -Name EncodedTicketSize -Value $data.Ticket.EncodedTicketSize
                        $obj | Add-Member -MemberType NoteProperty -Name EncodedTicket -Value $EncodedTicket
                    
                        Write-Output $obj
                    }
                    else
                    {
                    
                    }                    
                }
                else
                {
                    $WinErrorCode = LsaNtStatusToWinError -NtStatus $success
                    $LastError = [ComponentModel.Win32Exception]$WinErrorCode
                    throw "LsaCallAuthenticationPackage Error: $($LastError.Message)"
                }        
            }
        }
    }

    function LsaConnectUntrusted
    {
        <#
        .SYNOPSIS

        The LsaConnectUntrusted function establishes an untrusted connection to the LSA server.

        .DESCRIPTION

        LsaConnectUntrusted returns a handle to an untrusted connection; it does not verify any information about the caller. The handle should be closed using the LsaDeregisterLogonProcess function.
    
        If your application simply needs to query information from authentication packages, you can use the handle returned by this function in calls to LsaCallAuthenticationPackage and LsaLookupAuthenticationPackage.
    
        Applications with the SeTcbPrivilege privilege may create a trusted connection by calling LsaRegisterLogonProcess.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect, LsaNtStatusToWinError (Function)
        Optional Dependencies: None

        (func secur32 LsaConnectUntrusted ([UInt32]) @(
            [IntPtr].MakeByRefType() #_Out_ PHANDLE LsaHandle
        ) -EntryPoint LsaConnectUntrusted)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa378265(v=vs.85).aspx

        .EXAMPLE

        $hLsa = LsaConnectUntrusted
        #>

        param
        (

        )
    
        $LsaHandle = [IntPtr]::Zero

        $SUCCESS = $Secur32::LsaConnectUntrusted([ref]$LsaHandle)

        if($SUCCESS -ne 0)
        {
            $WinErrorCode = LsaNtStatusToWinError -NtStatus $success
            $LastError = [ComponentModel.Win32Exception]$WinErrorCode
            throw "LsaConnectUntrusted Error: $($LastError.Message)"
        }

        Write-Output $LsaHandle
    }

    function LsaDeregisterLogonProcess
    {
        <#
        .SYNOPSIS

        The LsaDeregisterLogonProcess function deletes the caller's logon application context and closes the connection to the LSA server.

        .DESCRIPTION

        If your logon application references the connection handle after calling the LsaDeregisterLogonProcess function, unexpected behavior can result.
    
        .PARAMETER LsaHandle

        Handle obtained from a previous call to LsaRegisterLogonProcess or LsaConnectUntrusted.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect, LsaNtStatusToWinError (Function)
        Optional Dependencies: None

        (func secur32 LsaDeregisterLogonProcess ([UInt32]) @(
            [IntPtr] #_In_ HANDLE LsaHandle
        ) -EntryPoint LsaDeregisterLogonProcess)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa378269(v=vs.85).aspx

        .EXAMPLE

        $hLsa = LsaConnectUntrusted

        #
        # Do Somthing with the LSA Handle
        #
    
        LsaDeregisterLogonProcess -LsaHandle $hLsa
        #>

        param
        (
            [Parameter(Mandatory = $true)]
            [IntPtr]
            $LsaHandle
        )

        $SUCCESS = $Secur32::LsaDeregisterLogonProcess($LsaHandle)

        if($SUCCESS -ne 0)
        {
            $WinErrorCode = LsaNtStatusToWinError -NtStatus $success
            $LastError = [ComponentModel.Win32Exception]$WinErrorCode
            throw "LsaDeregisterLogonProcess Error: $($LastError.Message)"
        }
    }

    function LsaEnumerateLogonSessions
    {
        <#
        .SYNOPSIS

        The LsaEnumerateLogonSessions function retrieves the set of existing logon session identifiers (LUIDs) and the number of sessions.

        .DESCRIPTION

        To retrieve information about the logon sessions returned by LsaEnumerateLogonSessions, call the LsaGetLogonSessionData function.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect, LsaNtStatusToWinError (Function)
        Optional Dependencies: None

        (func secur32 LsaEnumerateLogonSessions ([UInt32]) @(
            [UInt64].MakeByRefType(), #_Out_ PULONG LogonSessionCount,
            [IntPtr].MakeByRefType()  #_Out_ PLUID  *LogonSessionList
        ) -EntryPoint LsaEnumerateLogonSessions)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa378275(v=vs.85).aspx

        .EXAMPLE

        LsaEnumerateLogonSessions
        8
        2390553591808

        .EXAMPLE

        $SessionCount, $LogonSessionListPtr = LsaEnumerateLogonSessions
        #>

        $LogonSessionCount = [UInt64]0
        $LogonSessionList = [IntPtr]::Zero

        $SUCCESS = $Secur32::LsaEnumerateLogonSessions([ref]$LogonSessionCount, [ref]$LogonSessionList)

        if($SUCCESS -ne 0)
        {
            $WinErrorCode = LsaNtStatusToWinError -NtStatus $success
            $LastError = [ComponentModel.Win32Exception]$WinErrorCode
            throw "LsaEnumerateLogonSessions Error: $($LastError.Message)"
        }

        $obj = New-Object -TypeName psobject

        $obj | Add-Member -MemberType NoteProperty -Name SessionCount -Value $LogonSessionCount
        $obj | Add-Member -MemberType NoteProperty -Name SessionListPointer -Value $LogonSessionList
    
        Write-Output $obj
    }

    function LsaFreeReturnBuffer
    {
        <#
        .SYNOPSIS

        The LsaFreeReturnBuffer function frees the memory used by a buffer previously allocated by the LSA.

        .DESCRIPTION

        Some of the LSA authentication functions allocate memory buffers to hold returned information, for example, LsaLogonUser and LsaCallAuthenticationPackage. Your application should call LsaFreeReturnBuffer to free these buffers when they are no longer needed.

        .PARAMETER Buffer

        Pointer to the buffer to be freed.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect, LsaNtStatusToWinError (Function)
        Optional Dependencies: None

        (func secur32 LsaFreeReturnBuffer ([UInt32]) @(
            [IntPtr] #_In_ PVOID Buffer
        ) -EntryPoint LsaFreeReturnBuffer)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa378279(v=vs.85).aspx

        .EXAMPLE

        LsaFreeReturnBuffer -Buffer $Buffer
        #>

        param
        (
            [Parameter(Mandatory = $true)]
            [IntPtr]
            $Buffer
        )

        $SUCCESS = $Secur32::LsaFreeReturnBuffer($Buffer)

        if($SUCCESS -ne 0)
        {
            $WinErrorCode = LsaNtStatusToWinError -NtStatus $success
            $LastError = [ComponentModel.Win32Exception]$WinErrorCode
            throw "LsaFreeReturnBuffer Error: $($LastError.Message)"
        }
    }

    function LsaGetLogonSessionData
    {
        <#
        .SYNOPSIS

        The LsaGetLogonSessionData function retrieves information about a specified logon session.

        .DESCRIPTION

        .Parameter LuidPointer

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect, LsaFreeReturnBuffer (Function), LsaNtStatusToWinError (Function), SECURITY_LOGON_SESSION_DATA (Structure), LUID (Structure), SecurityEntity (Enumeration) LSA_UNICODE_STRING (Structure), LSA_LAST_INTER_LOGON_INFO (Structure), SECURITY_LOGON_TYPE (Enumeration)
        Optional Dependencies: None

        (func secur32 LsaGetLogonSessionData ([UInt32]) @(
            [IntPtr],                #_In_  PLUID                        LogonId,
            [IntPtr].MakeByRefType() #_Out_ PSECURITY_LOGON_SESSION_DATA *ppLogonSessionData
        ) -EntryPoint LsaGetLogonSessionData)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa378290(v=vs.85).aspx

        .EXAMPLE

        $SessionCount, $LogonSessionListPtr = LsaEnumerateLogonSessions
        LsaGetLogonSessionData -LuidPointer $LogonSessionListPtr
        #>

        param
        (
            [Parameter(Mandatory = $true)]
            [IntPtr]
            $LuidPointer
        )

        $sessionDataPtr = [IntPtr]::Zero
        $SUCCESS = $Secur32::LsaGetLogonSessionData($LuidPointer, [ref]$sessionDataPtr)

        if($SUCCESS -ne 0)
        {
            $WinErrorCode = LsaNtStatusToWinError -NtStatus $SUCCESS
            $LastError = [ComponentModel.Win32Exception]$WinErrorCode
            throw "[LsaGetLogonSessionData] Error: $($LastError.Message)"
        }

        try
        {
            $sessionData = $sessionDataPtr -as $SECURITY_LOGON_SESSION_DATA

            if($sessionData.LogonId.LowPart -eq 996)
            {
                $Upn = [System.Runtime.InteropServices.Marshal]::PtrToStringUni([IntPtr]::Add($sessionData.Upn.Buffer, 2), $sessionData.Upn.Length / 2)
            }
            else
            {
                $Upn = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.Upn.Buffer, $sessionData.Upn.Length / 2)
            }
                            
            New-Object -TypeName psobject -Property @{
                LogonId = $sessionData.LogonId.LowPart
                UserName = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.Username.Buffer, $sessionData.Username.Length / 2)
                LogonDomain = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.LogonDomain.Buffer, $sessionData.LognDomain.Length / 2)
                AuthenticationPackage = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.AuthenticationPackage.Buffer, $sessionData.AuthenticationPackage.Length / 2)
                LogonType = $sessionData.LogonType -as $SECURITY_LOGON_TYPE
                Session = $sessionData.Session
                Sid = New-Object -TypeName System.Security.Principal.SecurityIdentifier($sessionData.PSiD)
                LogonTime = [datetime]::FromFileTime($sessionData.LogonTime)
                LogonServer = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.LogonServer.Buffer, $sessionData.LogonServer.Length / 2)
                DnsDomainName = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.DnsDomainName.Buffer, $sessionData.DnsDomainName.Length / 2)
                Upn =  [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.Upn.Buffer, $sessionData.Upn.Length / 2)
                UserFlags = $sessionData.UserFlags
                LastSuccessfulLogon = $sessionData.LastLogonInfo.LastSuccessfulLogon
                LastFailedLogon = $sessionData.LastLogonInfo.LastFailedLogon
                FailedAttemptCountSinceLastSuccessfulLogon = $sessionData.LastLogonInfo.FailedAttemptCountSinceLastSuccessfulLogon
                LogonScript = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.LogonScript.Buffer, $sessionData.LogonScript.Length / 2)
                ProfilePath = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.ProfilePath.Buffer, $sessionData.ProfilePath.Length / 2)
                HomeDirectory = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.HomeDirectory.Buffer, $sessionData.HomeDirectory.Length / 2)
                HomeDirectoryDrive = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($sessionData.HomeDirectoryDrive.Buffer, $sessionData.HomeDirectoryDrive.Length / 2)
                LogoffTime = $sessionData.LogoffTime
                KickOffTime = $sessionData.KickOffTime
                PasswordLastSet = [datetime]::FromFileTime($sessionData.PasswordLastSet)
                PasswordCanChange = [datetime]::FromFileTime($sessionData.PasswordCanChange)
                PasswordMustChange = $sessionData.PasswordMustChange
            }
        }
        catch
        {

        }

        LsaFreeReturnBuffer -Buffer $sessionDataPtr
    }

    function LsaLookupAuthenticationPackage
    {
        <#
        .SYNOPSIS

        The LsaLookupAuthenticationPackage function obtains the unique identifier of an authentication package.

        .DESCRIPTION

        The authentication package identifier is used in calls to authentication functions such as LsaLogonUser and LsaCallAuthenticationPackage.

        .PARAMETER LsaHandle

        Handle obtained from a previous call to LsaRegisterLogonProcess or LsaConnectUntrusted.

        .PARAMETER PackageName

        Specifies the name of the authentication package. Supported packages are 'MSV1_0_PACKAGE_NAME', 'MICROSOFT_KERBEROS_NAME_A', 'NEGOSSP_NAME_A', and 'NTLMSP_NAME_A'.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Function Dependencies: PSReflect, LsaNtStatusToWinError, LSA_STRING (Structure)
        Optional Dependencies: None

        (func secur32 LsaLookupAuthenticationPackage ([UInt32]) @(
            [IntPtr],                           #_In_  HANDLE      LsaHandle,
            $LSA_UNICODE_STRING.MakeByRefType() #_In_  PLSA_STRING PackageName,
            [UInt64].MakeByRefType()            #_Out_ PULONG      AuthenticationPackage
        ) -EntryPoint LsaLookupAuthenticationPackage)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa378297(v=vs.85).aspx

        .EXAMPLE

        $hLsa = LsaConnectUntrusted

        LsaLookupAuthenticationPackage -LsaHandle $hLsa -PackageName MICROSOFT_KERBEROS_NAME_A
        2
        #>

        param
        (
            [Parameter(Mandatory = $true)]
            [IntPtr]
            $LsaHandle,

            [Parameter(Mandatory = $true)]
            [ValidateSet('MSV1_0_PACKAGE_NAME', 'MICROSOFT_KERBEROS_NAME_A', 'NEGOSSP_NAME_A', 'NTLMSP_NAME_A')]
            [string]
            $PackageName
        )

        switch($PackageName)
        {
            MSV1_0_PACKAGE_NAME {$authPackageName = 'NTLM'; break}
            MICROSOFT_KERBEROS_NAME_A {$authPackageName = 'Kerberos'; break}
            NEGOSSP_NAME_A {$authPackageName = 'Negotiate'; break}
            NTLMSP_NAME_A {$authPackageName = 'NTLM'; break}
        }

        $authPackageArray = [System.Text.Encoding]::ASCII.GetBytes($authPackageName)
        [int]$size = $authPackageArray.Length
        [IntPtr]$pnt = [System.Runtime.InteropServices.Marshal]::AllocHGlobal($size) 
        [System.Runtime.InteropServices.Marshal]::Copy($authPackageArray, 0, $pnt, $authPackageArray.Length)
    
        $lsaString = [Activator]::CreateInstance($LSA_STRING)
        $lsaString.Length = [UInt16]$authPackageArray.Length
        $lsaString.MaximumLength = [UInt16]$authPackageArray.Length
        $lsaString.Buffer = $pnt
    
        $AuthenticationPackage = [UInt64]0

        $SUCCESS = $Secur32::LsaLookupAuthenticationPackage($LsaHandle, [ref]$lsaString, [ref]$AuthenticationPackage)
    
        if($SUCCESS -ne 0)
        {
            $WinErrorCode = LsaNtStatusToWinError -NtStatus $success
            $LastError = [ComponentModel.Win32Exception]$WinErrorCode
            throw "LsaLookupAuthenticationPackage Error: $($LastError.Message)"
        }

        [System.Runtime.InteropServices.Marshal]::FreeHGlobal($pnt)

        Write-Output $AuthenticationPackage
    }

    function LsaNtStatusToWinError
    {
        <#
        .SYNOPSIS

        The LsaNtStatusToWinError function converts an NTSTATUS code returned by an LSA function to a Windows error code.

        .PARAMETER NtStatus

        An NTSTATUS code returned by an LSA function call. This value will be converted to a System error code.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect
        Optional Dependencies: None

        (func advapi32 LsaNtStatusToWinError ([UInt64]) @(
            [UInt32] #_In_ NTSTATUS Status
        ) -EntryPoint LsaNtStatusToWinError)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/ms721800(v=vs.85).aspx

        .EXAMPLE
        #>

        [CmdletBinding()]
        param
        (
            [Parameter(Mandatory = $true)]
            [UInt32]
            $NtStatus
        )

        $STATUS = $Advapi32::LsaNtStatusToWinError($NtStatus)

        Write-Output $STATUS
    }

    function LsaRegisterLogonProcess
    {
        <#
        .SYNOPSIS

        The LsaLookupAuthenticationPackage function obtains the unique identifier of an authentication package.

        .DESCRIPTION

        The authentication package identifier is used in calls to authentication functions such as LsaLogonUser and LsaCallAuthenticationPackage.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect, LsaNtStatusToWinError (Function), LSA_STRING (Structure)
        Optional Dependencies: None

        (func secur32 LsaRegisterLogonProcess ([UInt32]) @(
            $LSA_STRING.MakeByRefType() #_In_  PLSA_STRING           LogonProcessName,
            [IntPtr].MakeByRefType()    #_Out_ PHANDLE               LsaHandle,
            [UInt64].MakeByRefType()    #_Out_ PLSA_OPERATIONAL_MODE SecurityMode
        ) -EntryPoint LsaRegisterLogonProcess)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa378297(v=vs.85).aspx

        .EXAMPLE

        $hLsa = LsaRegisterLogonProcess
        #>

        $lsaStringArray = [System.Text.Encoding]::ASCII.GetBytes("INVOKE-IR")
        [int]$size = $lsaStringArray.Length
        [IntPtr]$pnt = [System.Runtime.InteropServices.Marshal]::AllocHGlobal($size) 
        [System.Runtime.InteropServices.Marshal]::Copy($lsaStringArray, 0, $pnt, $lsaStringArray.Length)
    
        $lsaString = [Activator]::CreateInstance($LSA_STRING)
        $lsaString.Length = [UInt16]$lsaStringArray.Length
        $lsaString.MaximumLength = [UInt16]$lsaStringArray.Length
        $lsaString.Buffer = $pnt

        $LsaHandle = [IntPtr]::Zero
        $SecurityMode = [UInt64]0

        $SUCCESS = $Secur32::LsaRegisterLogonProcess([ref]$lsaString, [ref]$LsaHandle, [ref]$SecurityMode)

        if($SUCCESS -ne 0)
        {
            $WinErrorCode = LsaNtStatusToWinError -NtStatus $success
            $LastError = [ComponentModel.Win32Exception]$WinErrorCode
            throw "LsaRegisterLogonProcess Error: $($LastError.Message)"
        }

        Write-Output $LsaHandle
    }

    function OpenProcessToken
    { 
        <#
        .SYNOPSIS

        The OpenProcessToken function opens the access token associated with a process.

        .PARAMETER ProcessHandle

        A handle to the process whose access token is opened. The process must have the PROCESS_QUERY_INFORMATION access permission.

        .PARAMETER DesiredAccess

        Specifies an access mask that specifies the requested types of access to the access token. These requested access types are compared with the discretionary access control list (DACL) of the token to determine which accesses are granted or denied.
        For a list of access rights for access tokens, see Access Rights for Access-Token Objects.

        .NOTES
    
        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect
        Optional Dependencies: TOKEN_ACCESS (Enumeration)

        (func advapi32 OpenProcessToken ([bool]) @(
            [IntPtr],                #_In_  HANDLE  ProcessHandle
            [UInt32],                #_In_  DWORD   DesiredAccess
            [IntPtr].MakeByRefType() #_Out_ PHANDLE TokenHandle
        ) -EntryPoint OpenProcessToken -SetLastError)
        
        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa379295(v=vs.85).aspx
    
        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa374905(v=vs.85).aspx

        .EXAMPLE
        #>

        [OutputType([IntPtr])]
        [CmdletBinding()]
        param
        (
            [Parameter(Mandatory = $true)]
            [IntPtr]
            $ProcessHandle,
        
            [Parameter(Mandatory = $true)]
            [ValidateSet('TOKEN_ASSIGN_PRIMARY','TOKEN_DUPLICATE','TOKEN_IMPERSONATE','TOKEN_QUERY','TOKEN_QUERY_SOURCE','TOKEN_ADJUST_PRIVILEGES','TOKEN_ADJUST_GROUPS','TOKEN_ADJUST_DEFAULT','TOKEN_ADJUST_SESSIONID','DELETE','READ_CONTROL','WRITE_DAC','WRITE_OWNER','SYNCHRONIZE','STANDARD_RIGHTS_REQUIRED','TOKEN_ALL_ACCESS')]
            [string[]]
            $DesiredAccess  
        )
    
        # Calculate Desired Access Value
        $dwDesiredAccess = 0

        foreach($val in $DesiredAccess)
        {
            $dwDesiredAccess = $dwDesiredAccess -bor $TOKEN_ACCESS::$val
        }

        $hToken = [IntPtr]::Zero
        $Success = $Advapi32::OpenProcessToken($ProcessHandle, $dwDesiredAccess, [ref]$hToken); $LastError = [Runtime.InteropServices.Marshal]::GetLastWin32Error()

        if(-not $Success) 
        {
            throw "OpenProcessToken Error: $(([ComponentModel.Win32Exception] $LastError).Message)"
        }
    
        Write-Output $hToken
    }

    function RevertToSelf
    {
        <#
        .SYNOPSIS

        The RevertToSelf function terminates the impersonation of a client application.

        .DESCRIPTION

        A process should call the RevertToSelf function after finishing any impersonation begun by using the DdeImpersonateClient, ImpersonateDdeClientWindow, ImpersonateLoggedOnUser, ImpersonateNamedPipeClient, ImpersonateSelf, ImpersonateAnonymousToken or SetThreadToken function.
    
        An RPC server that used the RpcImpersonateClient function to impersonate a client must call the RpcRevertToSelf or RpcRevertToSelfEx to end the impersonation.
    
        If RevertToSelf fails, your application continues to run in the context of the client, which is not appropriate. You should shut down the process if RevertToSelf fails.

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: PSReflect
        Optional Dependencies: None

        (func advapi32 RevertToSelf ([bool]) @(
    
        ) -EntryPoint RevertToSelf -SetLastError)

        .LINK

        https://msdn.microsoft.com/en-us/library/windows/desktop/aa379317(v=vs.85).aspx

        .EXAMPLE

            [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
            NT AUTHORITY\SYSTEM

            RevertToSelf

            [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
            hunt.local\jared
        #>

        [CmdletBinding()]
        param
        (

        )

        $SUCCESS = $Advapi32::RevertToSelf(); $LastError = [Runtime.InteropServices.Marshal]::GetLastWin32Error()
    
        if(-not $SUCCESS)
        {
            throw "RevertToSelf Error: $(([ComponentModel.Win32Exception] $LastError).Message)"
        }
    }
    #endregion Win32 function abstractions

    #region Helper Functions
    function Get-LogonSession
    {
        <#

        .SYNOPSIS

        .DESCRIPTION

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: 
        Required Dependencies: PSReflect, LsaEnumerateLogonSessions (Function), LsaFreeReturnBuffer (Function), LsaGetLogonSessionData (Function) LsaNtStatusToWinError (Function), SECURITY_LOGON_SESSION_DATA (Structure), LUID (Structure), LSA_UNICODE_STRING (Structure), LSA_LAST_INTER_LOGON_INFO (Structure), SecurityEntity (Enumeration), SECURITY_LOGON_TYPE (Enumeration)
        Optional Dependencies: None

        .LINK

        .EXAMPLE

        Get-LogonSession

        FailedAttemptCountSinceLastSuccessfulLogon : 0
        DnsDomainName                              : HUNT.LOCAL
        KickOffTime                                : 1/1/1601 1:00:00 AM
        PasswordCanChange                          : 5/20/2017 9:51:20 PM
        Upn                                        : Administrator@HUNT.LOCAL
        UserName                                   : Administrator
        Session                                    : 1
        LogoffTime                                 : 1/1/1601 1:00:00 AM
        LastFailedLogon                            : 1/1/1601 1:00:00 AM
        LogonServer                                : DC
        Sid                                        : S-1-5-21-3250051078-751264820-3215766868-500
        LogonScript                                : 
        UserFlags                                  : 49444
        ProfilePath                                : 
        PasswordMustChange                         : 6/30/2017 9:51:20 PM
        LogonId                                    : 325349
        LogonTime                                  : 5/20/2017 9:47:34 AM
        PasswordLastSet                            : 5/19/2017 9:51:20 PM
        LogonDomain                                : 
        HomeDirectory                              : 
        LogonType                                  : Interactive
        AuthenticationPackage                      : Kerberos
        LastSuccessfulLogon                        : 1/1/1601 1:00:00 AM
        HomeDirectoryDrive                         : 

        #>

        [CmdletBinding()]
        param
        (

        )

        $LogonSessions = LsaEnumerateLogonSessions
    
        $CurrentPtr = $LogonSessions.SessionListPointer

        for($i = 0; $i -lt $LogonSessions.SessionCount; $i++)
        {
            try
            {
                # Retreive details about the current logon session
                LsaGetLogonSessionData -LuidPointer $CurrentPtr
            }
            catch
            {

            }

            # Increment to the next LUID
            $CurrentPtr = [IntPtr]::Add($CurrentPtr, $LUID::GetSize())
        }
    }

    function Get-System
    {
        <#
        .SYNOPSIS

        .DESCRIPTION

        .NOTES

        Author: Jared Atkinson (@jaredcatkinson)
        License: BSD 3-Clause
        Required Dependencies: None
        Optional Dependencies: None
        
        .LINK

        .EXAMPLE
        #>

        # Get a Process object for the winlogon process
        # The System.Diagnostics.Process class has a handle property that we can use
        # We know winlogon will be available and is running as NT AUTHORITY\SYSTEM
        $proc = Get-Process -Name winlogon

        if($proc.Length -gt 1)
        {
            $proc = $proc[0]
        }

        if($proc.Handle)
        {
            # Open winlogon's Token with TOKEN_DUPLICATE Acess
            # This allows us to make a copy of the token with DuplicateToken
            $hToken = OpenProcessToken -ProcessHandle $proc.Handle -DesiredAccess TOKEN_DUPLICATE -Debug
    
            # Make a copy of the NT AUTHORITY\SYSTEM Token
            $hDupToken = DuplicateToken -TokenHandle $hToken
    
            # Apply our Duplicated Token to our Thread
            ImpersonateLoggedOnUser -TokenHandle $hDupToken
    
            # Clean up the handles we created
            CloseHandle -Handle $hToken
            CloseHandle -Handle $hDupToken

            if([System.Security.Principal.WindowsIdentity]::GetCurrent().Name -ne 'NT AUTHORITY\SYSTEM')
            {
                throw "Unable to Impersonate System Token"
            }
        }
        else
        {
            throw "Unable to Impersonate System Token"
        }
    }
    #endregion Helper Functions
    
    try
    {
        # We need a Handle to LSA to list Kerberos tickets
        # If we want to look at tickets from a session other than our own
        # Then we need to use LsaRegisterLogonProcess instead of LsaConnectUntrusted
        $hLsa = LsaRegisterLogonProcess
    }
    catch
    {
        # If the original call fails then it is likely we don't have SeTcbPrivilege
        # To get SeTcbPrivilege we can Impersonate a NT AUTHORITY\SYSTEM Token
        Get-System
            
        # We should now have the proper privileges to get a Handle to LSA
        $hLsa = LsaRegisterLogonProcess

        # We don't need our NT AUTHORITY\SYSTEM Token anymore
        # So we can revert to our original token
        RevertToSelf
    }

    if($hLsa)
    {
        # Enumerate all Logon Sessions
        # We need the sessions' LogonIds to enumerate it
        $Sessions = Get-LogonSession

        foreach($Session in $Sessions)
        {
            # Get the tickets from the LSA provider
            $ticket = LsaCallAuthenticationPackage -LsaHandle $hLsa -AuthenticationPackageName MICROSOFT_KERBEROS_NAME_A -LogonId $Session.LogonId 
            
            if($ticket -ne $null)
            {
                # Add properties from the Logon Session to the ticket
                $ticket | Add-Member -MemberType NoteProperty -Name SessionLogonId -Value $Session.LogonId
                $ticket | Add-Member -MemberType NoteProperty -Name SessionUserName -Value $Session.UserName
                $ticket | Add-Member -MemberType NoteProperty -Name SessionUserPrincipalName -Value $Session.Upn
                $ticket | Add-Member -MemberType NoteProperty -Name SessionLogonType -Value ([string]$Session.LogonType)
                $ticket | Add-Member -MemberType NoteProperty -Name SessionAuthenticationPackage -Value $Session.AuthenticationPackage
                $ticket | Add-Member -MemberType NoteProperty -Name SessionLogonServer -Value $Session.LogonServer
                $ticket | Add-Member -MemberType NoteProperty -Name SessionLogonDomain -Value $Session.LogonDomain

                # Output the ticket
                Write-Output $ticket
            }
        }

        # Cleanup our LSA Handle
        LsaDeregisterLogonProcess -LsaHandle $hLsa
    }
}