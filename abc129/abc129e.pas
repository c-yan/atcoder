program abc129e;
var
  L: string;
  I, T, Result: Int64;
begin
  Read(L);

  Result := 1;
  T := 1;
  for I := Length(L) downto 1 do
  begin
    if L[i] = '1' then
    begin
      Result := Result * 2 + t;
      Result := Result mod 1000000007;
    end;
    T := T * 3;
    T := T mod 1000000007;
  end;
  WriteLn(Result);
end.
